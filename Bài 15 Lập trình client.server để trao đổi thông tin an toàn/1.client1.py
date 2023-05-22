import socket
import hashlib
HOST = "127.0.0.1"
SERVER_PORT = 65432
FORMAT = "utf8"


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print("ClINET SIDE")
client.connect((HOST,SERVER_PORT))
try:
    while True:
        data = input("Clinet gui toi Server: ")
        client.sendall(data.encode(FORMAT))

        if data == "quit" :break

        data_server = client.recv(1024).decode(FORMAT)
        print("Nhan tu Server : ",data_server)
finally:
    client.close()

# Ninh chí hướng _ B20DCAT094    