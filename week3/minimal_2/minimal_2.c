void gadgets() {
	asm volatile(
		"pop %rdi; ret;"
		"pop %rsi; ret;"
		"pop %rdx; ret;"
		"pop %r10; ret;"
		"pop %r8; ret;"
		"pop %r9; ret;"
		"syscall; ret;"
	);
}

void main() {
    asm volatile(
        "mov $0, %rax;"
        "mov $0, %rdi;"
        "mov %rsp, %rsi;"
        "mov $2000, %rdx;"
        "syscall;"
    );
}

int _start() {
	main();
    asm volatile(
    	"mov $60, %rax;"
    	"mov $0, %rdi;"
    	"syscall;"
    );
}
