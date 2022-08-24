#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void win() {
	puts("you win!! heres a shell");
	execve("/bin/sh", 0, 0);
	exit(0);
}

void vuln() {
	printf("username: ");
	fflush(0);
	char name[32];
	gets(name);
	printf("\n");
	printf("password: ");
	char pw[32];
	gets(pw);
	printf("\n");
	if(strcmp(name, "ag") == 0 && strcmp(pw, "reveille") == 0) {
		printf("Account correct! I'll see about sending the flag your way in 5 business days\n");
	} else {
		printf("That doesn't look right :(\n");
	}
}

void main() {
	setvbuf(stdout, 0, 2, 0);
	vuln();
}
