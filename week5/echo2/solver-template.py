from pwn import *

p = remote("128.199.12.141", 7014)

# automate inputs as necessary here

p.interactive()
