"""Echo server: sends back every message one client sends, until the client leaves.

Run (terminal 1): python 02_echo_server.py
Run (terminal 2): python 02_echo_client.py
The server serves one client. When that client disconnects, the server exits.
"""

import socket

HOST = "127.0.0.1"
PORT = 5002

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Echo server listening on {HOST}:{PORT} ...")

    connection, address = server.accept()
    with connection:
        print("Client connected from", address)
        while True:
            data = connection.recv(1024)
            if not data:                # empty bytes means the client closed
                break
            print("Received:", data.decode())
            connection.sendall(data)    # send the same bytes straight back

print("Client left. Server finished.")
