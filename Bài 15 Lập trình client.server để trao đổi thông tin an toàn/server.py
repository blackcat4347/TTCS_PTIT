# Ninh Chí Hướng-B20DCAT094
import socket
import hashlib

host = 'localhost'
port = 5000

key = "mysecretkey"

s = socket.socket()
s.bind((host, port))
s.listen(1)
print("Waiting for incoming connection...")

conn, addr = s.accept()
print("Connected to: ", addr)
while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print("From connected user: " + str(data))
    message = data + key
    h = hashlib.sha256(message.encode())
    result = h.hexdigest()
    conn.send(result.encode())
conn.close()