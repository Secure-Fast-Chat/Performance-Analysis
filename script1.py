from pwn import process
import os
import datetime
import time

# s = process(['python3', 'loadbalancer.py'],cwd='../Server-Side')
# time.sleep(1)
# print(s.recv().decode('utf-8'))

# p = []
n=100
# for i in range(100):
#     time.sleep(0.01)
#     p.append(process(['python3','../Client_Side/app.py']))
#     p[i].sendline(b'1')
#     p[i].sendline(str(i).encode('utf-8'))
#     p[i].sendline(str(i).encode('utf-8'))

p = process(['python3','../Client_Side/app.py'])
i=0
time.sleep(1)
p.recv()
p.sendline(b'1')
p.sendline(str(i).encode('utf-8'))
p.sendline(str(i).encode('utf-8'))
time.sleep(1)
# time.sleep(5)
# Users Logged in Successfully
# print(s.recv().decode('utf-8'))
print('reached')

p.sendline(b'\\mkgrp grp')
p.recv()
for i in range(1,10):
    time.sleep(0.03)
    p.sendline(b'\\addmem grp ' + str(i).encode('utf-8'))
p.sendline(b'\\logout')
time.sleep(3)
print(p.recv().decode('utf-8'))
