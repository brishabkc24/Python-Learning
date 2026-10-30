"""Client that retries up to five times, one second apart, when the server refuses the connection; the server starts late on purpose."""

import socket
import threading
import time

HOST = "127.0.0.1"
PORT = 5010
MAX_ATTEMPTS = 5


def run_server_later(delay):
    time.sleep(delay)       # the server is "down" for a while
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()
        connection, address = server.accept()
        with connection:
            connection.sendall(b"Thanks for waiting!")


def connect_with_retries():
    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((HOST, PORT))
            print(f"Attempt {attempt}: connected")
            return client
        except ConnectionRefusedError:
            client.close()
            print(f"Attempt {attempt}: server not available, retrying in 1 s")
            time.sleep(1)
    return None


server_thread = threading.Thread(target=run_server_later, args=(3.5,))
server_thread.start()

connection = connect_with_retries()
if connection is None:
    print("Giving up.")
else:
    with connection:
        print("Server says:", connection.recv(1024).decode())
    server_thread.join()
