"""Calculator server and client in one file: the client sends requests like add 2 3 and the server replies with the result until it receives quit."""

import socket
import threading
import time

HOST = "127.0.0.1"
PORT = 5007


def calculate(request):
    parts = request.split()
    if len(parts) != 3:
        return "error: use <operation> <number> <number>"
    operation, first, second = parts[0], float(parts[1]), float(parts[2])
    if operation == "add":
        return str(first + second)
    if operation == "sub":
        return str(first - second)
    if operation == "mul":
        return str(first * second)
    if operation == "div":
        if second == 0:
            return "error: division by zero"
        return str(first / second)
    return f"error: unknown operation {operation}"


def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()
        connection, address = server.accept()
        with connection:
            while True:
                request = connection.recv(1024).decode()
                if not request or request == "quit":
                    break
                connection.sendall(calculate(request).encode())


server_thread = threading.Thread(target=run_server)
server_thread.start()
time.sleep(0.5)

requests = ["add 2 3", "mul 4 2.5", "div 7 0", "pow 2 3", "quit"]
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    for request in requests:
        client.sendall(request.encode())
        if request == "quit":
            print("Client: quit")
            break
        print(f"{request} -> {client.recv(1024).decode()}")

server_thread.join()
