# Ninh Chí Hướng-B20DCAT094
import socket
import hashlib

host = 'localhost'
port = 5000

key = "mysecretkey"

s = socket.socket()
s.connect((host, port))

while True:
    message = input("Enter data to hash: ")
    message_with_key = message + key
    h = hashlib.sha256(message_with_key.encode())
    message_hash = h.hexdigest()
    s.send(message_hash.encode())
    result = s.recv(1024).decode()
    if result == "Data integrity verified":
        print("Data integrity verified")
    else:
        print("The received message has lost its integrity.")
    key = input("Enter new key: ")
    message_with_new_key = message + key
    h = hashlib.sha256(message_with_new_key.encode())
    message_hash_with_new_key = h.hexdigest()
    s.send(message_hash_with_new_key.encode())
    result = s.recv(1024).decode()
    print("Data: " + message)
    if result == "Data integrity verified":
        print("Data integrity verified with new key")
    else:
        print("The received message has lost its integrity with new key.")
    
s.close()