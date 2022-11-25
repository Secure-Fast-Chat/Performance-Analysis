
from pwn import process
import os
import datetime
import time
import random

p=[]
for x,i in enumerate([50,51]):
    time.sleep(0.01)
    p.append(process(['python3','../Client_Side/app.py']))
    p[x].sendline(b'1')
    p[x].sendline(str(i).encode('utf-8'))
    p[x].sendline(str(i).encode('utf-8'))

time.sleep(2)
# Users Logged in Successfully
# print(s.recv().decode('utf-8'))
print('reached')
while True:
    time.sleep(0.5)
    i = random.randint(0,1)
    p[i].sendline(f'\\send {50+1-i} {str(datetime.datetime.timestamp(datetime.datetime.now()))}')
