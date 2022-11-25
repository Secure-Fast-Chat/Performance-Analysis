
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
try:
    while True:
        time.sleep(random.gauss(0.5,0.15))
        i = random.randint(0,1)
        p[i].sendline(f'\\send {50+1-i} {str(datetime.datetime.timestamp(datetime.datetime.now()))}')
except KeyboardInterrupt:
    os.system("sed -ne '/Recieved/p' SecureFastChatlogs_50.txt | cut -d ':' -f 1 > 50_recv_time")
    os.system("sed -ne '/Recieved/p' SecureFastChatlogs_51.txt | cut -d ':' -f 1 > 51_recv_time")
    os.system("sed -ne '/Sent/p' SecureFastChatlogs_50.txt | cut -d ':' -f 1 > 50_send_time")
    os.system("sed -ne '/Sent/p' SecureFastChatlogs_51.txt | cut -d ':' -f 1 > 51_send_time")
    os.system("awk '{count++;if (NR==FNR) {sum[0]+=$1} else {sum[1]+=$1}}END{print(sum[0]-sum[1]);print(count)}' 50_recv_time 51_send_time")
    os.system("awk '{count++;if (NR==FNR) {sum[0]+=$1} else {sum[1]+=$1}}END{print(sum[0]-sum[1]);print(count)}' 51_recv_time 50_send_time")
