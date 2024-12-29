#!/bin/bash

# listen on port 12345 and store received information to a file
nc -l -p 12345 > received_data.txt