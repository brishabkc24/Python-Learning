"""Chat server: takes turns with one client; the chat ends when someone types bye.

Run (terminal 1): python 05_chat_server.py
Run (terminal 2): python 05_chat_client.py
The client speaks first. Sample session on the server side:
    Client: hello
    You: hi there
    Client: bye
"""

import socket

HOST = "127.0.0.1"
PORT = 5005

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Chat server listening on {HOST}:{PORT} ...")

    connection, address = server.accept()
    with connection:
        print("Client connected. Waiting for the first message.")
        while True:
            data = connection.recv(1024)
            if not data:
                print("Client disconnected.")
                break
            message = data.decode()
            print("Client:", message)
            if message == "bye":
                print("Client said bye. Chat over.")
                break

            reply = input("You: ")
            connection.sendall(reply.encode())
            if reply == "bye":
                print("You ended the chat.")
                break
