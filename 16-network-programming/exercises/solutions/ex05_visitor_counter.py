"""Threaded visitor-counter server: every client gets You are visitor number N; three clients connect at the same time."""

import socket
import threading
import time

HOST = "127.0.0.1"
PORT = 5009

visitor_count = 0
count_lock = threading.Lock()


def handle_client(connection):
    global visitor_count
    with connection:
        with count_lock:                # two clients must not get the same number
            visitor_count += 1
            number = visitor_count
        connection.sendall(f"You are visitor number {number}".encode())


def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()
        while True:
            connection, address = server.accept()
            threading.Thread(target=handle_client, args=(connection,)).start()


def run_client(name):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        print(f"{name} got: {client.recv(1024).decode()}")


# daemon=True: the server loops forever, but the program may still end.
threading.Thread(target=run_server, daemon=True).start()
time.sleep(0.5)

clients = [threading.Thread(target=run_client, args=(name,)) for name in ["Aarav", "Sita", "Bikash"]]
for client_thread in clients:
    client_thread.start()
for client_thread in clients:
    client_thread.join()

print("Total visitors:", visitor_count)
