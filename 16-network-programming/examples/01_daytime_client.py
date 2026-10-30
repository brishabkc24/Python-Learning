"""Daytime client: connects to the daytime server and prints the time it sends.

Run: python 01_daytime_client.py   (start 01_daytime_server.py first)
If the server is not running, a clear message is printed instead of a crash.
"""

import socket

HOST = "127.0.0.1"
PORT = 5001

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        data = client.recv(1024)                # up to 1024 bytes
        print("Server time:", data.decode())    # bytes back to text
except ConnectionRefusedError:
    print(f"Could not connect to {HOST}:{PORT}. Is the server running?")
