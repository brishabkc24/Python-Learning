"""
Chat Client
===========
Connects to the chat server on 127.0.0.1:5050. It asks for your name
(or takes it from the command line), then every line you type is sent
to the server, and messages from the other people arrive as they are
typed. Type bye to leave.

Run: python client.py            (server.py must already be running)
     python client.py Asha       (skips the name question)

Sample session:
    Your name: Asha
    Welcome, Asha! Type bye to leave.
    *** Bikash joined the chat (127.0.0.1:53114)
    Bikash: hello everyone
    hi Bikash
    bye
    Disconnected from the server.
"""

import socket
import sys
import threading

HOST = "127.0.0.1"
PORT = 5050


def receive_messages(connection):
    """Run in a thread: print every line the server sends until it closes."""
    try:
        reader = connection.makefile("r", encoding="utf-8")
        for line in reader:
            print(line.rstrip())
    except OSError:
        pass                      # the socket was closed while we were reading
    print("Disconnected from the server.")


def send_line(connection, text):
    connection.sendall((text + "\n").encode("utf-8"))


def get_name():
    """Use the first command-line argument as the name, or ask for one."""
    if len(sys.argv) > 1:
        return sys.argv[1].strip() or "Guest"
    return input("Your name: ").strip() or "Guest"


def main():
    name = get_name()

    try:
        connection = socket.create_connection((HOST, PORT))
    except ConnectionRefusedError:
        print("Could not connect. Start server.py first.")
        return

    send_line(connection, name)
    receiver = threading.Thread(target=receive_messages, args=(connection,), daemon=True)
    receiver.start()

    try:
        while True:
            text = input()
            send_line(connection, text)
            if text.strip().lower() == "bye":
                break
    except (KeyboardInterrupt, EOFError):
        send_line(connection, "bye")      # leave politely if the input ends
    finally:
        # Tell the server we are done sending, wait for the goodbye, then close.
        connection.shutdown(socket.SHUT_WR)
        receiver.join(timeout=2)
        connection.close()


if __name__ == "__main__":
    main()
