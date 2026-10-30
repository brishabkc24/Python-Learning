"""
Chat Server
===========
Accepts any number of chat clients on 127.0.0.1:5050. Each client is
handled in its own thread. Every message is sent to all the other
clients with the sender's name in front. A client that sends "bye" is
disconnected. Press Ctrl+C to stop the server.

Run: python server.py        (then start client.py in other terminals)
"""

import socket
import threading

HOST = "127.0.0.1"
PORT = 5050

clients = {}                      # socket -> name
clients_lock = threading.Lock()   # threads must not change the dict at the same time


def send_line(connection, text):
    """Send one line to one client; ignore clients that already went away."""
    try:
        connection.sendall((text + "\n").encode("utf-8"))
    except OSError:
        pass


def broadcast(text, exclude=None):
    """Send a line to every connected client except 'exclude'."""
    print(text)                   # the server terminal shows the whole conversation
    with clients_lock:
        receivers = [conn for conn in clients if conn is not exclude]
    for connection in receivers:
        send_line(connection, text)


def handle_client(connection, address):
    """Run in a thread: read lines from one client until it says bye."""
    reader = connection.makefile("r", encoding="utf-8")
    name = reader.readline().strip() or "Guest"

    with clients_lock:
        clients[connection] = name
    send_line(connection, f"Welcome, {name}! Type bye to leave.")
    broadcast(f"*** {name} joined the chat ({address[0]}:{address[1]})", exclude=connection)

    for line in reader:           # ends when the client closes the connection
        text = line.strip()
        if text.lower() == "bye":
            break
        if text:
            broadcast(f"{name}: {text}", exclude=connection)

    with clients_lock:
        clients.pop(connection, None)
    broadcast(f"*** {name} left the chat")
    connection.close()


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    # A timeout makes accept() return regularly, so Ctrl+C is noticed on every system.
    server.settimeout(1.0)
    print(f"Chat server listening on {HOST}:{PORT}. Press Ctrl+C to stop.")

    try:
        while True:
            try:
                connection, address = server.accept()
            except socket.timeout:
                continue
            worker = threading.Thread(target=handle_client, args=(connection, address), daemon=True)
            worker.start()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    finally:
        server.close()


if __name__ == "__main__":
    main()
