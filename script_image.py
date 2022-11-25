from pwn import process
import random
import os
import datetime
import time
import os

# s = process(['python3', 'loadbalancer.py'],cwd='../Server-Side')
# time.sleep(2)
# print(s.recv().decode('utf-8'))

p = []
n=10
for i in range(n):
    time.sleep(0.01)
    p.append(process(['python3','../Client_Side/app.py']))
    p[i].sendline(b'1')
    p[i].sendline(str(i).encode('utf-8'))
    p[i].sendline(str(i).encode('utf-8'))


time.sleep(5)
# Users Logged in Successfully

while True:
    i = random.randint(0,8)
    print(i)
    try:
        time.sleep(random.gauss(0.5,0.1))
        sendMsgCommand = '\send 9 '+ str(datetime.datetime.timestamp(datetime.datetime.now()))
        k = random.random()
        print(k)
        if k>0.1:
            p[i].sendline(sendMsgCommand.encode('utf-8'))
        else:
            p[i].sendline(b'\sendfile 1 images.png')
    except KeyboardInterrupt:
        print(p[i].recv())
        print(i)
        break
