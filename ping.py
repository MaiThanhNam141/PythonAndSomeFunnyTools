import socket

source_ip = "172.16.1.255"  # Thay thế bằng địa chỉ IP của máy nguồn
source_port = 5000

# Địa chỉ IP và cổng của máy chủ hoặc thiết bị đích
server_ip = "26.50.28.52"
server_port = 135

# Số lần gửi gói tin
num_packets = 100

# Dữ liệu gửi trong gói tin (có thể thay đổi nội dung)
data_to_send = b"Hello, server!"

# Tạo một đối tượng socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.bind((source_ip, source_port))
    # Kết nối đến máy chủ hoặc thiết bị đích
    
    client_socket.connect((server_ip, server_port))

    # Gửi gói tin nhiều lần
    for _ in range(num_packets):
        client_socket.send(data_to_send)

    print(f"Sent {num_packets} packets to {server_ip}:{server_port}")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Đóng kết nối
    client_socket.close()
