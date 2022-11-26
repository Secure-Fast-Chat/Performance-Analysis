from pwn import process
import random
import os
import datetime
import time
import os
import argparse

# s = process(['python3', 'loadbalancer.py'],cwd='../Server-Side')
# time.sleep(2)
# print(s.recv().decode('utf-8'))

parser = argparse.ArgumentParser()
parser.add_argument("--num_users", type = int, required = True)
parser.add_argument("--ratio_img_senders", type = float, required = True)
args = parser.parse_args()


p = []
n=args.num_users
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
    i = random.randint(0,n-1)
    try:
        time.sleep(abs(random.gauss(0.1,0.05)))
        sendMsgCommand = '\send ' + str(random.randint(0,n+5)) +' '+ '0'*random.randint(0,400)
        k = random.random()
        print(k)
        # p[i].sendline(sendMsgCommand.encode('utf-8'))
        if k>args.ratio_img_senders:
            p[i].sendline(sendMsgCommand.encode('utf-8'))
        else:
            p[i].sendline('\sendfile ' +str(random.randint(0,n+5)) + ' image.jpg')
    except KeyboardInterrupt:
        print(i)
        break
    except Exception as e:
        time.sleep(2)
        print(p[i].recv())
        print(e)

time.sleep(10)
os.system("cat SecureFastChatlogs_* | grep Rec | cut -d ':' -f 1 > recv_time")
os.system(f"cat SecureFastChatlogs_* | grep Sent | grep -v 'Message Sent to {n}'| grep -v 'Message Sent to {n+1}'| grep -v 'Message Sent to {n+2}'| grep -v 'Message Sent to {n+3}'| grep -v 'Message Sent to {n+4}'| grep -v 'Message Sent to {n+5}'|cut -d ':' -f 1 > send_time")
# os.system("awk '{if(FR==NFR){countr++;sumr+=$1}else{counts++;sums+=$1}}END{print(sumr-sums);print(countr,counts)}' recv_time send_time")
os.system("awk '{count++;if(NR==FNR){countr++;sumr+=$1} else {if(counts<countr){counts++;sums+=$1}}}END{print(sumr-sums);print(countr);print(counts)}' recv_time send_time")

# os.system("rm SecureFastChat*")
