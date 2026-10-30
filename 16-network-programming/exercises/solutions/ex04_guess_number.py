"""Guessing game over a socket: the server keeps a secret number and answers too high, too low or correct to each guess."""

import socket
import threading
import time

HOST = "127.0.0.1"
PORT = 5008
SECRET = 42


def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()
        connection, address = server.accept()
        with connection:
            while True:
                data = connection.recv(1024)
                if not data:
                    break
                guess = int(data.decode())
                if guess > SECRET:
                    answer = "too high"
                elif guess < SECRET:
                    answer = "too low"
                else:
                    answer = "correct"
                connection.sendall(answer.encode())
                if answer == "correct":
                    break


server_thread = threading.Thread(target=run_server)
server_thread.start()
time.sleep(0.5)

guesses = [50, 25, 37, 43, 42]
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    for attempt, guess in enumerate(guesses, start=1):
        client.sendall(str(guess).encode())
        answer = client.recv(1024).decode()
        print(f"Guess {attempt}: {guess} -> {answer}")
        if answer == "correct":
            print(f"Found the number in {attempt} guesses.")
            break

server_thread.join()
