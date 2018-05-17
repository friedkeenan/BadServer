import socket
import sys
s=socket.socket()
stuff=list(sys.argv[1])
stuff.reverse()
stuff=''.join(stuff).split(":",1)
for i in range(2):
    t=list(stuff[i])
    t.reverse()
    t=''.join(t)
    stuff[i]=t
s.connect((socket.gethostbyname(stuff[1]),int(stuff[0])))
s.send(sys.argv[2].encode())
print(s.recv(1024).decode())
s.close()
