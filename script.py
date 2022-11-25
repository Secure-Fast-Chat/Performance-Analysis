from pwn import process
import os
import datetime
import time

# s = process(['python3', 'loadbalancer.py'],cwd='../Server-Side')
# time.sleep(2)
# print(s.recv().decode('utf-8'))

p = []
n=100
for i in range(100):
    time.sleep(0.01)
    p.append(process(['python3','../Client_Side/app.py']))
    p[i].sendline(b'1')
    p[i].sendline(str(i).encode('utf-8'))
    p[i].sendline(str(i).encode('utf-8'))

time.sleep(5)
# Users Logged in Successfully
# print(s.recv().decode('utf-8'))
print('reached')
for i in range(100):
    # time.sleep(0.03)
    try:
        p[i].sendline(b'\send 1 '+ str(datetime.datetime.timestamp(datetime.datetime.now())).encode('utf-8'))
    except:
        print(i)
        continue


time.sleep(5)

os.system("awk '{sum += $1-$2} END{print(sum)}' SecureFastChatMessages_1.txt")
os.system('rm SecureFastChat*')

# for i in range(100):
#     time.sleep(0.02)
#     try:
#         p[i].sendline(b'\send 1 '+ str(datetime.datetime.timestamp(datetime.datetime.now())).encode('utf-8'))
#     except:
#         print(i)
#         continue
# 
# 
# time.sleep(7)
# 
# os.system("awk '{sum += $1-$2} END{print(sum)}' SecureFastChatMessages_1.txt")
# os.system('rm SecureFastChat*')
# for i in range(100):
#     # time.sleep(0.05)
#     try:
#         p[i].sendline(b'\send 1 '+ str(datetime.datetime.timestamp(datetime.datetime.now())).encode('utf-8'))
#     except:
#         print(i)
#         continue
# 
# 
# time.sleep(10)
# 
# os.system("awk '{sum += $1-$2} END{print(sum)}' SecureFastChatMessages_1.txt")
# os.system('rm SecureFastChat*')
