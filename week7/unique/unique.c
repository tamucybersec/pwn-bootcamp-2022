#include <sys/mman.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// All unique bytes shellcode except I couldn't figure out how to handle null bytes so you can have as many of those as you want
void check(char* code) {
    char bad[256];
    memset(bad, 0, 256);
    int bad_size = 0;

    for(int i = 0; i < 0x1000; i++) {
        if (code[i] == '\x00') {
            continue;
        }
        if (strchr(bad, code[i]) != NULL) {
            exit(-1);
        }
        bad[bad_size] = code[i];
        bad_size++;
    }
}


int main() {
    void (*code)() = mmap(NULL, 0x1000, PROT_EXEC|PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0);
    fgets((char*)code, 0x1000, stdin);
    check((char*)code);
    code();
}

