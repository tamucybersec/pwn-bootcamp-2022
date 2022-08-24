#include <stdio.h>
void vuln() {
	char buf[8];
	fgets(buf, 24, stdin);
}


void query() {
	malloc(4096 * 4);
	printf("whats you're name?\n");
	char* name = malloc(256);
	fgets(name, 256, stdin);
	printf("nice to meet you %s!  i left your name tag at 0x%lx\n", name, name);
	vuln();
}

void main() {
	setvbuf(stdout, 0, _IONBF,0);
	setvbuf(stdin, 0, _IONBF,0);
	setvbuf(stderr, 0, _IONBF,0);
	query();
}
