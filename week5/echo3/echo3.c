#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include <seccomp.h>

void main() {

 	scmp_filter_ctx ctx = seccomp_init(SCMP_ACT_ALLOW);
 	seccomp_rule_add(ctx, SCMP_ACT_KILL, 59, 0);
 	seccomp_load(ctx);
	setvbuf(stdout, 0, _IONBF,0);
	setvbuf(stdin, 0, _IONBF,0);
	setvbuf(stderr, 0, _IONBF,0);

	while(1) {
		char buf[64];
		memset(buf, 0, 64);
		fgets(buf, 64, stdin);
		printf(buf);
		if(strcmp(buf,"n") == 0) { exit(0); }
	}
	
}
