#include <stdio.h>
void main() {
	setvbuf(stdout, 0, _IONBF,0);
	setvbuf(stdin, 0, _IONBF,0);
	setvbuf(stderr, 0, _IONBF,0);

	char flag[64];
	FILE* f = fopen("flag.txt", "r");
	if(f == 0) {
		printf("make a dummy flag file :)\n");
		exit(1);
	}
	fgets(flag, 64, f);

	char buf[64];
	memset(buf, 0, 64);
	fgets(buf, 64, stdin);
	printf(buf);
}
