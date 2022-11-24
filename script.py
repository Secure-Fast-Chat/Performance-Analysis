from pwn import process
import os
import datetime
import time

# os.chdir('../Server-Side')
# s = process(['python3', 'loadbalancer.py'])
p = []
n=100
for i in range(100):
    p.append(process(['python3','../Client_Side/app.py']))
    p[i].sendline(b'1')
    p[i].sendline(str(i).encode('utf-8'))
    p[i].sendline(str(i).encode('utf-8'))

time.sleep(5)
print('reached')
for i in range(100):
    try:
        p[i].sendline(b'\send 0 '+ str(datetime.datetime.timestamp(datetime.datetime.now())).encode('utf-8'))
    except:
        print(i)
        continue

time.sleep(5)
