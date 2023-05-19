# Ninh chí hướng _ B20DCAT094
import socket
import hashlib

key = "mysecretkey"

# Kết nối tới server
s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host, port))

# Gửi thông điệp kèm mã băm
message = input("Nhap thong diep: ")
message_bytes = message.encode()
key_bytes = key.encode()
hash_object = hashlib.md5(message_bytes + key_bytes)
hash_digest = hash_object.digest()
s.send(message_bytes + hash_digest)

# Nhận phản hồi từ server
response = s.recv(1024).decode()
if response == "Integrity verified.":
    print("Server response:", response)
else:
    print("The received message has lost its integrity.")

# Đóng kết nối
s.close()