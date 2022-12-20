#if 0
OUTFILE=$(basename "$0" .c)
gcc $0 -o "$OUTFILE"
./"$OUTFILE"
rm "$OUTFILE"
exit
#endif

// ^^ Thought it was cool, can execute the file like normal bash script, but c preprocessor ignores it
// compiles the file (only outputs errors), runs it, then deletes it
// would be cool to see if I can pass commandline arguments to the file
#include <stdio.h>

int main (int argc, char *argv[])
{
  int a;
  printf("Running this C file!\n");
  return 0;
}
