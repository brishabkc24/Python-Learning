"""Welcome client: sends your name to the server and prints the greeting it returns.

Run: python 03_welcome_client.py   (start 03_welcome_server.py first)
Sample session:
    Your name: Sita
    Server says: Welcome, Sita! Nice to meet you.
"""

import socket

HOST = "127.0.0.1"
PORT = 5003

name = input("Your name: ")

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        client.sendall(name.encode())
        reply = client.recv(1024)
        print("Server says:", reply.decode())
except ConnectionRefusedError:
    print(f"Could not connect to {HOST}:{PORT}. Is the server running?")
