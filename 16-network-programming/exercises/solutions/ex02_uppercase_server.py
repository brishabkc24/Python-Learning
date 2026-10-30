"""Uppercase server and client in one file: the client sends a sentence and the server replies with it in upper case."""

import socket
import threading
import time

HOST = "127.0.0.1"
PORT = 5006


def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()
        connection, address = server.accept()
        with connection:
            data = connection.recv(1024)
            print("Server received:", data.decode())
            connection.sendall(data.decode().upper().encode())


# The server runs in a background thread so this exercise is one file.
server_thread = threading.Thread(target=run_server)
server_thread.start()
time.sleep(0.5)     # give the server a moment to start listening

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    client.sendall("python makes networking simple".encode())
    reply = client.recv(1024)
    print("Client got:     ", reply.decode())

server_thread.join()
