#include <sys/mman.h>
#include <stdio.h>
#include <stdlib.h>

// No syscalls bruh
void check(char* code) {
    for(int i = 0; i < 0x1000-1; i++) {
        if (code[i] == '\x0f' && code[i+1] == '\x05') {
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
