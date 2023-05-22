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
    message, received_hash = data.split("|")
    message_with_key = message + key
    h = hashlib.sha256(message_with_key.encode())
    calculated_hash = h.hexdigest()
    if calculated_hash == received_hash:
        conn.send("1".encode())
        print("Hash: " + received_hash)
        print("Received from client: " + message)
        print("Data integrity verified")
    else:
        conn.send("0".encode())
        print("The received message has lost its integrity.")
conn.close()