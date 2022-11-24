from pwn import process
import os
import datetime
import time

# os.chdir('../Server-Side')
# s = process(['python3', 'loadbalancer.py'])
p = []
n=10
for i in range(n):
    p.append(process(['python3','../Client_Side/app.py']))
    print(p[i].recvuntil(")\n"))
    print(p[i].recvuntil(":"))

    # Signup
    # print(p[i].recvuntil(":"))
    # p[i].sendline(b'2')
    # print(p[i].recvuntil(":"))
    # p[i].sendline(str(i).encode('utf-8'))
    # print(p[i].recvuntil(":"))
    # p[i].sendline(str(i).encode('utf-8'))
    # print(p[i].recvuntil(":"))
    # p[i].sendline(str(i).encode('utf-8'))
    # Login
    print("i###########Login###########")
    print(p[i].recvuntil(":"))
    p[i].sendline(b'1')
    print(p[i].recvuntil(":"))
    p[i].sendline(str(i).encode('utf-8'))
    print(p[i].recvuntil(":"))
    p[i].sendline(str(i).encode('utf-8'))
    print(p[i].recvuntil("In"))

time.sleep(2)

print('reached')
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
for i in range(n):
    print("Logging out")
    logout = "\logout"
    p[i].sendline(logout.encode('utf-8'))

