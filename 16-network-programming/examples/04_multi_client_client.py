"""Client for the multi-client server: sends three messages and prints the replies.

Run: python 04_multi_client_client.py   (start 04_multi_client_server.py first)
Run it in two or three terminals at once to see the server use one
thread per client.
"""

import socket
import time

HOST = "127.0.0.1"
PORT = 5004
MESSAGES = ["hello", "how are you", "goodbye"]

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        for message in MESSAGES:
            client.sendall(message.encode())
            reply = client.recv(1024)
            print("Server:", reply.decode())
            time.sleep(0.5)     # stay connected a moment so clients overlap
    print("Done.")
except ConnectionRefusedError:
    print(f"Could not connect to {HOST}:{PORT}. Is the server running?")
