import socket

HOST = "127.0.0.1" #loppback
SERVER_PORT = 65432
FORMAT = "utf8"
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((HOST,SERVER_PORT))
s.listen(1)

conn, addr = s.accept()

try:
    print("Client address:",addr)
    while True:
        data_client = conn.recv(1024).decode(FORMAT)
        print("Nhan tu client: ",data_client)
        if data_client == "quit" : break
        data = input("Server gui toi client: ")
        conn.sendall(data.encode(FORMAT))
finally:
    s.close()
# Ninh Chí Hướng _ B20DCAT094