import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))
    server_socket.listen(1)
    print("Server listening on port 12345")

    while True:
        try:
            client_socket, client_address = server_socket.accept()

            data = client_socket.recv(1024).decode()
            print(f"Received: {data}")
            client_socket.send("Data received".encode())
        except ConnectionAbortedError as e:
            print(f"Connection aborted: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            client_socket.close()

if __name__ == "__main__":
    start_server()