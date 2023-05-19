# Ninh Chí Hướng _ B20DCAT094
import socket
import hashlib

key = "mysecretkey"

# Khởi tạo server socket
s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))

# Chờ kết nối từ client
s.listen(1)
conn, addr = s.accept()

# Nhận thông điệp và mã băm từ client
data = conn.recv(1024)
received_message = data[:-16]  # Lấy thông điệp từ phần đầu của dữ liệu nhận được
received_hash = data[-16:]    # Lấy mã băm từ phần cuối của dữ liệu nhận được

# Kiểm tra tính toàn vẹn của thông điệp
key_bytes = key.encode()
hash_object = hashlib.md5(received_message + key_bytes)
hash_digest = hash_object.digest()
if hash_digest == received_hash:
    conn.send("Integrity verified.".encode())
else:
    conn.send("The received message has lost its integrity.".encode())

# Đóng kết nối
conn.close()
s.close()