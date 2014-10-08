#! /bin/sh -e

. /lib/lsb/init-functions

do_start()
{
    log_action_begin_msg "Loading iptables rules"

    # Create /var/run/iptables.d if it doesn't exist
    if [ ! -d /var/run/iptables.d ]; then
	mkdir /var/run/iptables.d
    fi

    files=`find /etc/iptables.d/ /var/run/iptables.d/ -type f | sed -re '/^.*~$/d;/^.*\/[.].*/d;/^.*README$/d;s/(^.*\/)([^\/]*)$/\2\ [\1\2\]/' | sort | sed -re 's/^.* \[(.*)\]/\1/'`
    for script in $files; do
	if [ -O $script ]; then
	    log_action_cont_msg "... loading:  ${script}"
		# This seems to be only way to actually get IFS to be newline
	    IFS="
"
		# Drop all comment lines and execute all others
	    for line in `cat $script | sed -re '/^\s*#+(.*)$/d'`; do
		unset IFS
		iptables ${line} > /dev/null 2>&1 || {
		    log_warning_msg "Rule returned error:
   '$line'"
		}
		IFS="
"
	    done
	else
	    log_warning_msg "... skipping: ${script} because not owned by this process"
	fi
    done;
    
    log_action_end_msg 0
}

do_stop()
{
    log_action_begin_msg "Flushing iptables rules"

    # Set default policy to accept
    iptables -P INPUT ACCEPT
    iptables -P OUTPUT ACCEPT
    iptables -P FORWARD ACCEPT
    iptables -F
    iptables -X

    for table in filter nat mangle; do
	iptables -t $table -F
	iptables -t $table -X
	iptables -t $table -Z
    done

    log_action_end_msg 0

}

case "$1" in
    start)
	do_start
	;;

    stop)
	do_stop
	;;
    
    restart)
	do_stop
	do_start
	;;
    *)
	echo "Usage: $0 {start|stop|restart}"
	exit 1
	;;
esac
exit 0
