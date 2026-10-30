"""Chat client: takes turns with the server; the chat ends when someone types bye.

Run: python 05_chat_client.py   (start 05_chat_server.py first)
You speak first. Sample session on the client side:
    You: hello
    Server: hi there
    You: bye
"""

import socket

HOST = "127.0.0.1"
PORT = 5005

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        print("Connected. Type bye to end the chat.")
        while True:
            message = input("You: ")
            client.sendall(message.encode())
            if message == "bye":
                print("You ended the chat.")
                break

            data = client.recv(1024)
            if not data:
                print("Server disconnected.")
                break
            reply = data.decode()
            print("Server:", reply)
            if reply == "bye":
                print("Server said bye. Chat over.")
                break
except ConnectionRefusedError:
    print(f"Could not connect to {HOST}:{PORT}. Is the server running?")
