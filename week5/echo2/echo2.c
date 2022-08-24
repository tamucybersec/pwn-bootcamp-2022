#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
bool authorized = false;


void win() {
	char flag[64];
	FILE* f = fopen("flag.txt", "r");
	if(f == 0) {
		printf("make a dummy flag file :)\n");
		exit(1);
	}
	fgets(flag, 64, f);
	printf(flag);
}

void main() {
	setvbuf(stdout, 0, _IONBF,0);
	setvbuf(stdin, 0, _IONBF,0);
	setvbuf(stderr, 0, _IONBF,0);


	printf("enter the password to get the flag!\n");
	while(1) {
		char buf[64];
		memset(buf, 0, 64);
		fgets(buf, 64, stdin);
		printf(buf);
		if(authorized) {
			win();
		}
	}
	
}
