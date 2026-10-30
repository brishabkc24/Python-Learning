"""Welcome server: receives the client's name and replies with a greeting.

Run (terminal 1): python 03_welcome_server.py
Run (terminal 2): python 03_welcome_client.py
The server serves one client and then exits.
"""

import socket

HOST = "127.0.0.1"
PORT = 5003

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Welcome server listening on {HOST}:{PORT} ...")

    connection, address = server.accept()
    with connection:
        name = connection.recv(1024).decode().strip()
        print(f"{name} connected from {address}")
        greeting = f"Welcome, {name}! Nice to meet you."
        connection.sendall(greeting.encode())

print("Server finished.")
