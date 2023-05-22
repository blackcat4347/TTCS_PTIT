# Ninh Chí Hướng-B20DCAT094
import socket
import hashlib

host = 'localhost'
port = 5000

key = "secretkey"

s = socket.socket()
s.connect((host, port))

while True:
    message = input("Enter data to send: ")
    message_with_key = message + key
    h = hashlib.sha256(message_with_key.encode())
    message_hash = h.hexdigest()
    data = message + "|" + message_hash
    s.send(data.encode())
    result = s.recv(1024).decode()
    if result == "1":
        print("Hash: " + message_hash)
        print("Received from server: " + message)
        print("Data integrity verified")
    else:
        print("The received message has lost its integrity.")

        
s.close()