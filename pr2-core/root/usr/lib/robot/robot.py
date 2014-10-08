#!/usr/bin/env python
        
from __future__ import with_statement

#from optparse import OptionParser
import os
import sys
import stat
import subprocess
import pwd
import grp
import signal
import time
import yaml
import socket
import string

from optparse import OptionParser
import UserDict

USERNAME = 'ros'
PID_FILE = '/var/tmp/ros.pid'
ACTIVE_USER_FILE = '/var/lib/robot/active_user.yaml'
TEST_WRITE_FILE = '/var/lib/robot/testwrite'
MIN_UID=1000


class RobotCmds(UserDict.UserDict):
    def __init__(self):
        UserDict.UserDict.__init__(self)
        self['help'] = (self.help_cmd, "Display this message")


    def get_valid_cmds(self):
        str = "Valid commands:\n"
        for k in sorted(self.keys()):
            if len(self[k][1]) > 0:
                str += "    * %s\t%s\n"%(k,self[k][1])
        return str

    def help_cmd(self,argv):
        argv = [a for a in argv if a != '-h' and a != '--help']

        if len(argv) == 0:
            print """Usage: robot <command> [options] [args]
"""
            print self.get_valid_cmds()
        else:
            cmd = argv[0]
            if cmd in self:
                print "Calling %s with -h"%cmd
                self[cmd][0](["-h"])
            else:
                print >> sys.stderr, "Invalid command: %s"%cmd
                print >> sys.stderr, ""
                print >> sys.stderr, self.get_valid_cmds()

def generate_env_loader():
    print
    resp = raw_input("Would you like to create an env-loader? (y/n): ")
    if resp.lower()=='y':
        print
        setup = raw_input("Enter the path to your setup.sh file: ")
        while not os.path.exists(os.path.expandvars(os.path.expanduser(setup))):
            setup = raw_input("%s does not exist. Enter the path to your setup file: "%setup)
        path = os.path.dirname(setup)
        path = os.path.expanduser(path)
        path = os.path.expandvars(path)
        path = os.path.join(path, "env.sh")
        print
        resp = raw_input("Would you like to use your current ROS_PACKAGE_PATH? (y/n): ")

        # while path is invalid
        while os.path.exists(path) or not os.access(os.path.dirname(path), os.W_OK):
            if not os.access(os.path.dirname(path), os.W_OK):
                print
                path = raw_input("%s isn't writable. Enter a path for your env-loader: "%path)
                path = os.path.expanduser(path)
                path = os.path.expandvars(path)
            elif os.path.exists(path):
                print
                replace = raw_input("%s exists. Would you like to replace it? (y/n): "%path)
                if replace.lower()=="y":
                    os.remove(path)
                else:
                    print
                    path = raw_input("Enter a path for your env-loader: ")
                    path = os.path.expanduser(path)
                    path = os.path.expandvars(path)

        # write file
        output = open(path, "w")

        output.write('#/bin/sh\n')
        output.write(". %s\n"%setup)
        if resp.lower()=='y':
            output.write("export ROS_PACKAGE_PATH=\"%s\"\n"%os.getenv('ROS_PACKAGE_PATH'))

        output.write("exec \"$@\"\n")

        output.close()

        # set executable
        os.chmod(path, stat.S_IXUSR | stat.S_IRUSR | stat.S_IWUSR)

        print
        print "Your env-loader has been created as %s."%path
        print "Please add 'export ROS_ENV_LOADER=\"%s\"' to your .bashrc"%path
    else:
        print
        print "No ROS_ENV_LOADER set and no env-loader created."


def cmd_claim(argv):
    parser = OptionParser(usage="robot claim",
                          description="Take ownership of the robot.  This will place your username in the file %s."%ACTIVE_USER_FILE)

    parser.add_option("-m", "--message", action="store", type="string", default=None, dest="message",
                      help="A message that will be shown to other users to let them know what you are doing with the robot.")
    parser.add_option("--email", action="store", type="string", default=None, dest="email",
                      help="An email address where you can be contacted.")

    parser.add_option("-u", "--username", action="store", type="string", default=None, dest="user",
                      help="Use a different username when claiming the robot.")
    parser.add_option("-f", "--force",   action="store_true", dest="force",
                      help="Don't warn if you are claiming from another user.")

    (options,args) = parser.parse_args(argv)

    checkslave()

    claim(options.user, options.email, options.message, options.force)



def cmd_release(argv):
    parser = OptionParser(usage="robot release",
                          description="Release ownership of the robot.  This will remove your username from the file %s."%ACTIVE_USER_FILE)
    parser.add_option("-u", "--username", action="store", type="string", default=None, dest="user",
                      help="Use a different username when claiming the robot.")
    parser.add_option("-f", "--force",   action="store_true", dest="force",
                      help="Don't warn if you are releasing the robot from another user.")

    (options,args) = parser.parse_args(argv)

    checkslave()

    if not check_claim(options.user, options.force):
        sys.exit(2)

    print "Releasing control of the robot."

    try:
        os.remove(ACTIVE_USER_FILE)
    except OSError, e:
        pass



def cmd_start(argv):
    parser = OptionParser(usage="robot start",
                          description="Bring up the robot.  This will first kill all processes running on the robot and then launch /etc/ros/robot.launch as a daemonized process.")


    parser.add_option("--system", action="store_true",  dest="system",
                      help="Run as the system user '%s' using the environment from: /etc/ros/setup.sh"%USERNAME)

    parser.add_option("--debug",   action="store_true", dest="debug",
                      help="Don't daemonize.")

    parser.add_option("-u", "--username", action="store", type="string", default=None, dest="user",
                      help="Use a different username when claiming the robot.")
    parser.add_option("-f", "--force",   action="store_true", dest="force",
                      help="Don't warn if you are claiming from another user.")

    (options,args) = parser.parse_args(argv)

    checkslave()

    if not check_claim(options.user, options.force):
        sys.exit(2)

    if not options.system:
        if 'ROS_ROOT' not in os.environ:
            print >> sys.stderr, "ROS_ROOT not set"
            sys.exit(1)
        
        if 'ROS_PACKAGE_PATH' not in os.environ:
            print >> sys.stderr, "ROS_PACKAGE_PATH not set"
            sys.exit(1)

        if 'ROS_MASTER_URI' not in os.environ:
            print >> sys.stderr, "ROS_MASTER_URI not set"
            sys.exit(1)

        if 'ROS_ENV_LOADER' not in os.environ:
            if "fuerte" in os.environ['ROS_PACKAGE_PATH']:
                print
                print "ROS_ENV_LOADER not set; see http://ros.org/wiki/roslaunch/XML/machine#Examples"
                print
                print "Would you like to use the default env-loader?"
                resp = raw_input("You will not be able to run custom software (y/n): ")
                if resp.lower()=='y':
                    os.environ['ROS_ENV_LOADER'] = '/etc/ros/env.sh'
                else:
                    os.setegid(os.getgid())
                    os.seteuid(os.getuid())
                    generate_env_loader()
                    sys.exit(1)

        env = os.environ

    else:
        env = {}
        
        newenv = subprocess.Popen('. /etc/ros/setup.sh; env', shell=True, executable='/bin/sh', env=env, stdout=subprocess.PIPE).communicate()[0]
        for k,v in [l.split('=') for l in newenv.splitlines()]:
            env[k] = v

        env['USER']=USERNAME
        env['HOME']=pwd.getpwnam(USERNAME).pw_dir

    # ckill implicitly requires a claim
    if ckill_prompt(options.force):
        ckill()

        print "Using environment:"
        print "ROS_ROOT="+env['ROS_ROOT']
        print "ROS_PACKAGE_PATH="+env['ROS_PACKAGE_PATH']
        print "USER="+env['USER']
        print "HOME="+env['HOME']
        if env.has_key('LIBRARY_PATH'):
            print "LD_LIBRARY_PATH="+env['LIBRARY_PATH']

        print "Launching necessary ROS processes in background."
        print "Check your pr2_dashboard for status information."

        if not options.debug:
            daemonize()

        os.setegid(os.getgid())
        os.seteuid(os.getuid())

        if env.has_key('LIBRARY_PATH'):
            env['LD_LIBRARY_PATH'] = env['LIBRARY_PATH']

        if options.system:
            subprocess.Popen(['sudo', '-u', 'ros', '/usr/lib/robot/roslaunch_ros', '--pid', PID_FILE], env=env)
        else:
            subprocess.Popen(['roslaunch', '/etc/ros/robot.launch', '--pid', PID_FILE], env=env)

        sys.exit(0)


def cmd_stop(argv):
    parser = OptionParser(usage="robot stop",
                          description="Bring down the robot.  This will kill all processes running on the robot.")

    parser.add_option("-u", "--username", action="store", type="string", default=None, dest="user",
                      help="Use a different username when claiming the robot.")
    parser.add_option("-f", "--force",   action="store_true", dest="force",
                      help="Don't warn if you are claiming from another user.")

    (options,args) = parser.parse_args(argv)

    checkslave()

    if not check_claim(options.user, options.force):
        sys.exit(2)


    if ckill_prompt(options.force):
        ckill()

        print "If you are done using the robot, it is recommended that you run 'robot release'"

    sys.exit(0)

def cmd_love(argv):
    p = subprocess.Popen(['fortune', 'love'], stdout=subprocess.PIPE)
    (out, err) = p.communicate()
    print """
          |  \ \ | |/ /
          |  |\ `' ' /
          |  ;'      \      / ,
          | ;    _,   |    / / ,
          | |   (  `-.;_,-' '-' ,
          | `,   `-._       _,-'_
          |,-`.    `.)    ,<_,-'_,
         ,'    `.   /   ,'  `;-' _,
        ;        `./   /`,    \-'
        |         /   |  ;\   |\\
        |        ;_,._|_,  `, ' \\
        |        \    \ `       `,
        `      __ `    \         ;,
         \   ,'  `      \,       ;;
          \_(            ;,      ;;
          |  \           `;,     ;;
          |  |`.          `;;,   ;'
          |  |  `-.        ;;;;,;' FL
          |  |    |`-.._  ,;;;;;'
          |  |    |   | ``';;;'
"""
    print out
    sys.exit(0)


def cmd_users(argv):
    parser = OptionParser(usage="robot users",
                          description="Display a list containing the current active user as well as all other users with active processes on the robot.")

    parser.add_option("--no-plist",   action="store_true", dest="noplist",
                      help="Don't check the plist when printing users information")

    (options,args) = parser.parse_args(argv)

    users(options.noplist)
    sys.exit(0)




def send_mail(address, subject, msg):
    sendmail_location = "/usr/sbin/sendmail" # sendmail location
    p = os.popen("%s -t" % sendmail_location, "w")
    p.write("To: %s\n" % address)
    p.write("From: %s <root@%s>\n" % (socket.gethostname(),socket.gethostname()))
    p.write("Subject: %s\n" % subject)
    p.write("\n") # blank line separating headers from body
    if msg is not None:
        p.write("%s"%msg)
    else:
        p.write("No message specified.")
    status = p.close()


def users(noplist=False):
    users = {}

    print ""

    a = load_active()
    if a is not None:
        print a
    else:
        print 'Active User: None'

    if not noplist:
        ckill_list = plist()
        if ckill_list is not None:
            for node in ckill_list:
                if not node: continue
                machine, _, _, user, _, bin, _, cmd = node.split(None, 7)
                if user in users:
                    users[user] += 1
                else:
                    users[user] = 1

            print ""

            if len(users.keys()) > 0:
                print "The following users have running processes:"
                for key,val in users.iteritems():
                    print " * %s (%d)"%(key,val)
            else:
                print "No non-system processes running."

        else:
            print >> sys.stderr, "Could not get listing of users"

    print ""


def cmd_plist(argv):
    parser = OptionParser(usage="robot plist",
                          description="Display the list of processes running on the robot.")

    (options,args) = parser.parse_args(argv)

    kill_list = plist()

    if kill_list is not None:
        if len(kill_list) > 0:
            print "The following processes are running:"
            for l in kill_list:
                print l
        else:
            print "No processes running."

        sys.exit(0)
    else:
        print >> sys.stderr, "Could not run ckill to check process list.  Check if c2 is reachable"
        sys.exit(3)


class ActiveUser(object):
    def __init__(self):
        self.user = None
        self.email = None
        self.message = None
        self.date = None

    def set_active(self):
        self.date=time.ctime()

        d = {}

        if self.user:
            d['user']=self.user

        if self.message:
            d['message']=self.message

        if self.email:
            d['email']=self.email

        if self.date:
            d['date']=self.date

        try:
            os.remove(ACTIVE_USER_FILE)
        except OSError, e:
            pass

        active = open(ACTIVE_USER_FILE,'w')
        active.write(yaml.dump(d, default_flow_style=False))
        active.close()

        return True

    def __str__(self):
        s = ""

        if self.user is not None:
            s += "Active User: %s"%self.user
        else:
            s += "Active User: None"

        if self.email:
            s += "\nContact: %s"%self.email

        if self.message:
            s += "\nMessage: %s"%self.message

        if self.date:
            s += "\nAcquired: %s"%self.date

        return s


def load_active():
    try:
        active = open(ACTIVE_USER_FILE)
        try:
            y = yaml.load(active)
        except:
            y = {}

        if y is None:
            y = {}

        active.close()

        a = ActiveUser()

        if 'user' in y:
            a.user = y['user']
        if 'message' in y:
            a.message = y['message']
        if 'email' in y:
            a.email = y['email']
        if 'date' in y:
            a.date = y['date']

        return a

    except IOError:
        return None


def kill_count():
    ckill_list = plist()
    
    if ckill_list is not None:
        return len(ckill_list)
    else:
        return None

def plist():
    ckill_list = subprocess.Popen(['sudo', 'ckill', 'list'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (o,e) = ckill_list.communicate()
    if ckill_list.returncode == 0:
        return o.splitlines()
#        return [l for l in o.splitlines() if not '/usr/lib/robot/robot.py' in l]
    else:
        return None

def check_claim(user, force):
    if force:
        return True

    this_user = ActiveUser()
    if 'USER' in os.environ:
        this_user.user=os.environ['USER']

    if user is not None:
        this_user.user=user

    old_active = load_active()

    if old_active is None or old_active.user != this_user.user:
        print >> sys.stderr, "To run this command you must first claim the robot: robot claim"
        return False

    return True

def claim(user, email, message, force):
    new_active = ActiveUser()

    new_active.user = "Unknown"
    if 'USER' in os.environ:
        new_active.user=os.environ['USER']
    if user is not None:
        new_active.user=user

    new_active.message=message

    new_active.email=email

    old_active = load_active()

    if old_active is None:
        print "Taking control of the robot."
        new_active.set_active()
    elif old_active.user != new_active.user:
        print "%s currently has control of the robot."%(old_active.user)
        if not force:
            while True:
                yesno = raw_input("Do you wish to replace them? [(y)es/(n)o]:")
                if yesno.lower()=="y" or yesno.lower()=="yes":
                    break
                elif yesno.lower()=="n" or yesno.lower()=="no":
                    print "Aborting..."
                    sys.exit(1)

        print "Stealing control of the robot from %s."%old_active.user
        if old_active.email is not None:
            send_mail(old_active.email,"Lost control of robot to: %s"%new_active.user,new_active.message)
        new_active.set_active()
    else: # Same user... claiming isn't necessary, unless we have a new message
        if (new_active.message is not None):
            new_active.set_active()

def ckill_prompt(force):
    if force:
        return True

    count = kill_count()

    if count is None:
        print >> sys.stderr, "Could not run ckill.  Check if c2 is up."
        sys.exit(3)

    if count > 0:
        users()
        print ""
        while True:
            yesno = raw_input("Kill these processes? [(y)es/(n)o/(s)how]:")
            if yesno.lower()=="y" or yesno.lower()=="yes":
                return True
            elif yesno.lower()=="n" or yesno.lower()=="no":
                print "Aborting..."
                return False
            elif yesno.lower()=='s' or yesno.lower()=='show':
                for l in plist():
                    print l
    else:
        return True



def ckill():
    count = kill_count()

    if count is None:
        print >> sys.stderr, "Could not run ckill."
        sys.exit(3)

    # Only need to actually do the killing if the count was > 0
    if count > 0:
        total_count = count
        total_progress = 50
        progress = 0.

        lev='SIGINT'
        print "Killing %d processes now..."%(total_count)


        print string.center("PROGRESS",total_progress,"=")

        # Start by killing all roslaunch processes
        subprocess.call(['sudo', 'ckill', 'kill', '--sig', lev, '--regex', 'python .*/roslaunch'])

        for lev in ['SIGINT','SIGTERM','SIGKILL','SIGKILL']:
            start = time.time()
            while True:
                while float(total_count - count)/total_count > progress/total_progress:
                    sys.stdout.write('#')
                    sys.stdout.flush()
                    progress += 1.

                if (count == 0):
                    break
                time.sleep(.1)
                last_count = count
                count = kill_count()
                if (count < last_count):
                    continue
                if (time.time() - start > 3):
                    subprocess.call(['sudo', 'ckill', 'kill', '--sig', lev])
                    break
        print ""
        if (count > 0):
            print "Some processes may have been left running:"
            for l in plist():
                print l
        else:
            print "All processes killed successfully."
    else:
        print "No processes to kill."


def daemonize (stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
        # Perform first fork.
    try:
        pid = os.fork( )
        if pid > 0:
            sys.exit(0) # Exit first parent.
    except OSError, e:
        sys.stderr.write("fork #1 failed: (%d) %sn" % (e.errno, e.strerror))
        sys.exit(1)
    # Decouple from parent environment.
    os.chdir("/")
    os.umask(0)
    os.setsid( )
    # Perform second fork.
    try:
        pid = os.fork( )
        if pid > 0:
            sys.exit(0) # Exit second parent.
    except OSError, e:
        sys.stderr.write("fork #2 failed: (%d) %sn" % (e.errno, e.strerror))
        sys.exit(1)
    # The process is now daemonized, redirect standard file descriptors.
    for f in sys.stdout, sys.stderr: f.flush( )
    si = file(stdin, 'r')
    so = file(stdout, 'a+')
    se = file(stderr, 'a+', 0)
    os.dup2(si.fileno( ), sys.stdin.fileno( ))
    os.dup2(so.fileno( ), sys.stdout.fileno( ))
    os.dup2(se.fileno( ), sys.stderr.fileno( ))


def checkslave():
    if (os.path.exists('/etc/slave')):
        print >> sys.stderr, "This robot command should not be run on c2."
        sys.exit(1)

def robotmain(argv=None):

    user_uid = os.getuid()
    if (user_uid == 0):
        print >> sys.stderr, "The robot command should no longer be run as root or with sudo."
        sys.exit(1)

    try:
        fd = open(TEST_WRITE_FILE,'w')
        fd.close()
        os.remove(TEST_WRITE_FILE)
    except IOError, e:
        print >> sys.stderr, "The robot command must be able to write to %s.  Check that %s and robot are both group robot, and that robot is setgid"%(ACTIVE_USER_FILE, ACTIVE_USER_FILE)
        sys.exit(1)


    cmds = RobotCmds()
    cmds['claim']    = (cmd_claim,   'Claim control of the robot.')
    cmds['release']  = (cmd_release, 'Release control of the robot.')
    cmds['start']    = (cmd_start,   'Start the robot (runs stop first if necessary).')
    cmds['stop']     = (cmd_stop,    'Stop all processes running on the robot and release control.')
    cmds['users']    = (cmd_users,   'Show all users on the robot.')
    cmds['plist']    = (cmd_plist,   'Show all processes running on the robot.')
    cmds['love']     = (cmd_love,   '')
    cmds['kill']     = (cmd_stop,    '')

    if argv is None:
        argv=sys.argv

    if '-h' in argv or '--help' in argv:
        argv = [a for a in argv if a != '-h' and a != '--help']
        argv.insert(1, 'help')

    if (len(argv) > 1):
        cmd = argv[1]
    else:
        cmd = 'help'

    if cmd in cmds:
        cmds[cmd][0](argv[2:])
    else:
        cmds['help'][0]([cmd])


if __name__ == '__main__':
    robotmain()

# vim: set ts=4 sw=4 expandtab:
