import socket
import sys
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ainfo = socket.getaddrinfo(None, 1234)
print(ainfo)
print(ainfo[3][4])

mysock.bind(ainfo[3][4])
mysock.listen(5)

while True:
    conn, addr = mysock.accept()
    data = conn.recv(1024)
    if not data:
        break
    print("Got a request!")
    print(data)
conn.close()
ms.close()
