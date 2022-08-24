
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

char* FLAG;

void shred() {
	struct {
		char data[100];
		int dev_null;
    } locals;
	;
	locals.dev_null = open("/dev/null", 1);
	gets(locals.data);
	write(locals.dev_null, FLAG, strlen(FLAG));
	write(locals.dev_null, locals.data, strlen(locals.data));
	close(locals.dev_null);
}

int main() {
	  	setvbuf(stdout, NULL, _IONBF, 0);
	    FILE* flag = fopen("flag.txt", "r");
        FLAG = malloc(64);
        if(flag == NULL) {
            strcpy(FLAG,"Flag file is missing, run that exploit again on the server!");
        } else {
            fgets(FLAG, 64, flag);
        }
        printf("%s\n", "Reading data for disposal:");
        shred();
}
