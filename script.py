from pwn import process
import os
import datetime
import time
import os

# s = process(['python3', 'loadbalancer.py'],cwd='../Server-Side')
# time.sleep(2)
# print(s.recv().decode('utf-8'))

p = []
n=100
for i in range(n):
    time.sleep(0.01)
    p.append(process(['python3','../Client_Side/app.py']))
    # print(p[i].recvuntil(")\n"))
    # print(p[i].recvuntil(":"))

    #Signup
    # print(p[i].recvuntil(":"))
    # p[i].sendline(b'2')
    # print(p[i].recvuntil(":"))
    # p[i].sendline(str(i).encode('utf-8'))
    # print(p[i].recvuntil(":"))
    # p[i].sendline(str(i).encode('utf-8'))
    # print(p[i].recvuntil(":"))
    # p[i].sendline(str(i).encode('utf-8'))
    # Login
    # print("i###########Login###########")
    # print(p[i].recvuntil(":"))
    p[i].sendline(b'1')
    # print(p[i].recvuntil(":"))
    p[i].sendline(str(i).encode('utf-8'))
    # print(p[i].recvuntil(":"))
    p[i].sendline(str(i).encode('utf-8'))
    # print(p[i].recvuntil("In"))


time.sleep(5)
# Users Logged in Successfully
# print(s.recv().decode('utf-8'))
for i in range(n):
    try:
        print(p[i].recv())
        sendMsgCommand = '\send 0 '+ str(datetime.datetime.timestamp(datetime.datetime.now()))
        print(sendMsgCommand)
        p[i].sendline(sendMsgCommand.encode('utf-8'))
        # p[0].recv()
    except Exception as e:
        print(i)
        print(e)
        continue


time.sleep(5)

# with open(os.path.join(os.path.expanduser('~'),'SecureFastChatMessages.txt'), 'r') as f:
#     lines = f.readlines()
#     timediff = 0
#     for line in lines:
#         print(line)
#         times = line.split("\t")
#         timediff += -float(times[0]) + float(times[1])
#     latency = timediff/len(lines)
#     print(f"latency = {latency}")
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
for i in range(n):
    print("Logging out")
    logout = "\logout"
    p[i].sendline(logout.encode('utf-8'))

