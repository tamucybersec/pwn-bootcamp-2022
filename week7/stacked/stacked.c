#include <sys/mman.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Only allowed these bytes, so good luck
char good[] = "\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x0f\x05";
 
void check(char* code) {
    for(int i = 0; i < 0x1000; i++) {
        if (code[i] == '\n') {
            break;
        }
        if (strchr(good, code[i]) == NULL) {
            exit(-1);
        }
    }
}


int main() {
    void (*code)() = mmap(NULL, 0x1000, PROT_EXEC|PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0);
    fgets((char*)code, 0x1000, stdin);
    check((char*)code);
    code();
}
