from pwn import process
import random
import os
import datetime
import time

# s = process(['python3', 'loadbalancer.py'],cwd='../Server-Side')
# time.sleep(2)
# print(s.recv().decode('utf-8'))

p = []
n=100
for i in range(10):
    time.sleep(0.01)
    p.append(process(['python3','../Client_Side/app.py']))
    p[i].sendline(b'1')
    p[i].sendline(str(i).encode('utf-8'))
    p[i].sendline(str(i).encode('utf-8'))

time.sleep(5)
# Users Logged in Successfully
# print(s.recv().decode('utf-8'))
print('reached')

t = 1
while True:
    time.sleep(t)
    i = random.randint(0,9)
    # print(i)
    # print(p[i])
    p[i].sendline(f'\\sendgrp grp {i} I am Here {str(datetime.datetime.timestamp(datetime.datetime.now()))}')
