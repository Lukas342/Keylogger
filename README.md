# Keylogger Project

## Overview
This project consists of a keylogger and mouse logger that captures keystrokes, and sends the data to a server. The server receives the data and writes it to a file.

## Project Structure
- `Server/`
    - `testSocket.py`: Python script to start the server and handle incoming data.
    - `record.sh`: Shell script to run the server and redirect output to `received.txt`.
    - `received.txt`: File where the received data is stored.
- `main.pyw`: Python script for the keylogger and mouse logger.
- `main.exe`: Executable version of the python script.

## Setup and Usage

### Server
1. Navigate to the `Server` directory.
2. Run the server using the shell script: `./record.sh`.
     Alternatively, you can run the server directly: `python testSocket.py`.

### Keylogger
1. Ensure the server is running.
2. Run the keylogger: `./main.exe.`
    Alternatively, you can run the keylogger directly: `python main.pyw`
        

## Dependencies
- < python 3.13
- `pynput` library for capturing keyboard and mouse events.

Install the required dependencies using pip:
```sh
pip install pynput
```

## Notes
- The server listens on port `12345` and writes received data to `received.txt`.
- The keylogger sends data to the server at `192.168.0.6:12345`. Update the `server_address` in `main.pyw` if needed.
- The project may get blocked by your anti-virus

### Recompile Executable
To recompile the executable if `main.pyw` has changed, use the following command:
```sh
pyinstaller --onefile --windowed main.pyw
```

## Disclaimer
This project is for educational purposes only. Ensure you have permission before using this software on any system.