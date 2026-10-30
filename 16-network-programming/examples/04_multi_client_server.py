"""Multi-client server: one thread per client, runs until you press Ctrl+C.

Run (terminal 1): python 04_multi_client_server.py
Run (terminals 2, 3, ...): python 04_multi_client_client.py
Several clients can be connected at the same time, each served by its
own thread. The server loops forever; stop it with Ctrl+C.
"""

import socket
import threading

HOST = "127.0.0.1"
PORT = 5004


def handle_client(connection, address):
    thread_name = threading.current_thread().name
    print(f"[{thread_name}] connected: {address}")
    with connection:
        while True:
            data = connection.recv(1024)
            if not data:
                break
            message = data.decode()
            print(f"[{thread_name}] received: {message}")
            connection.sendall(f"{thread_name} got: {message}".encode())
    print(f"[{thread_name}] disconnected: {address}")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    # accept() would block forever; a one-second timeout lets the loop
    # wake up regularly so Ctrl+C is noticed on every operating system.
    server.settimeout(1.0)
    print(f"Server listening on {HOST}:{PORT}. Press Ctrl+C to stop.")

    client_count = 0
    try:
        while True:
            try:
                connection, address = server.accept()
            except TimeoutError:
                continue                        # nobody connected; check again
            client_count += 1
            worker = threading.Thread(
                target=handle_client,
                args=(connection, address),
                name=f"Client-{client_count}",
                daemon=True,
            )
            worker.start()
    except KeyboardInterrupt:
        print("\nServer stopped.")
