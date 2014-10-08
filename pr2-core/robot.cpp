#include <unistd.h>

int main(int argc, char** argv)
{
  execvp("/usr/lib/robot/robot.py", argv);
}
