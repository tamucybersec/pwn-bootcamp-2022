#include <stdio.h>
#include <stdlib.h>


void gadgets() {
	asm("add $8, %rsp;");
}

void main() {
	setvbuf(stdout, 0, _IONBF,0);
	setvbuf(stdin, 0, _IONBF,0);
	setvbuf(stderr, 0, _IONBF,0);
	puts("hi lol");
	char buf[8 * 4];
	void (*exit_cached)(int, int, int);
	exit_cached = exit;
	fgets(buf, 8 * 6, stdin);
	exit_cached(1,2,3);
	return 1;
}
