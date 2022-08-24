#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void main() {
	setvbuf(stdout, 0, 2, 0);
	char buf[128];
	printf("Sally sells sea shells on the sea shore. There are 0x%lx sea shells on display, which one would you like?\n", buf);
	gets(buf);
}
