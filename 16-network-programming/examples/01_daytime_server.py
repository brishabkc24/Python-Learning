"""Daytime server: sends the current date and time to one client, then exits.

Run (terminal 1): python 01_daytime_server.py
Run (terminal 2): python 01_daytime_client.py
Start the server first. It serves one client and then stops.
"""

import socket
from datetime import datetime

HOST = "127.0.0.1"      # this computer only
PORT = 5001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    # Lets us restart the server right away after it closes.
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Daytime server listening on {HOST}:{PORT} ...")

    connection, address = server.accept()       # waits for a client
    with connection:
        print("Client connected from", address)
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        connection.sendall(now.encode())        # text must be sent as bytes
        print("Sent:", now)

print("Server finished.")
