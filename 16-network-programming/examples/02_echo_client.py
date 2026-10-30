"""Echo client: type messages, the server sends each one back. Type quit to stop.

Run: python 02_echo_client.py   (start 02_echo_server.py first)
Sample session:
    You: hello
    Echo: hello
    You: quit
"""

import socket

HOST = "127.0.0.1"
PORT = 5002

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        print("Connected. Type quit to stop.")
        while True:
            message = input("You: ")
            if message == "quit":
                break
            client.sendall(message.encode())
            reply = client.recv(1024)
            print("Echo:", reply.decode())
    print("Disconnected.")
except ConnectionRefusedError:
    print(f"Could not connect to {HOST}:{PORT}. Is the server running?")
