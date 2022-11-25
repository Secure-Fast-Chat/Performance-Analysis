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
    p[i].recv()



time.sleep(2)
p[1].recv()
# Users Logged in Successfully

count = 0
while True:
    count+=1
    if count == 20:
        os.system('rm SecureFastChat*')
    if count == 169:
        break
    i = random.randint(0,8)
    try:
        time.sleep(random.gauss(0.5,0.1))
        sendMsgCommand = '\send 9 '+ str(datetime.datetime.timestamp(datetime.datetime.now()))
        k = random.random()
        print(k)
        # p[i].sendline(sendMsgCommand.encode('utf-8'))
        if k>0.1:
            p[i].sendline(sendMsgCommand.encode('utf-8'))
        else:
            p[i].sendline(b'\sendfile 9 image.jpg')
    except KeyboardInterrupt:
        print(i)
        break
    except:
        time.sleep(2)
        print(p[i].recv())
        print(e)

time.sleep(10)
os.system("cat SecureFastChatlogs_* | grep Rec | cut -d ':' -f 1 > recv_time")
os.system("cat SecureFastChatlogs_* | grep Sent | cut -d ':' -f 1 > send_time")
# os.system("awk '{if(FR==NFR){countr++;sumr+=$1}else{counts++;sums+=$1}}END{print(sumr-sums);print(countr,counts)}' recv_time send_time")
os.system("awk '{count++;if(NR==FNR){countr++;sumr+=$1} else {if(counts<countr){counts++;sums+=$1}}}END{print(sumr-sums);print(countr);print(counts)}' recv_time send_time")

os.system("rm SecureFastChat*")
