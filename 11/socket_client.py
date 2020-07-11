import os
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, True) # added line
s.connect(("localhost", 20001))
while True:
    msg = input()
    s.send(msg.encode('utf8'))
    print(s.recv(8192))
