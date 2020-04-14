import socket

client = socket.socket()

client.connect(('127.0.0.1',8181))


client.sendall("bwei good".encode(encoding='utf-8'))

while True:
    msg = client.recv(1024)
    print(msg)
    if not msg:
        break
