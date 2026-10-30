# Network Programming

Network programming is writing programs that talk to each other over a network, such as a web browser talking to a web server. This topic uses Python's `socket` module to build small servers and clients that run on your own computer.

## What you will learn

- What a network, the client-server model, IP addresses, ports and protocols are
- The difference between TCP and UDP
- What a socket is and what `bind`, `listen`, `accept`, `connect`, `send`, `recv` and `close` do
- Writing a daytime server, an echo server and a welcome server with their clients
- Serving many clients at once with one thread per client
- A two-way chat between a server and a client
- Handling `ConnectionRefusedError` and other common errors
- How to run a server and a client in two terminals

## 1. What is a network?

A **network** is a group of computers connected so they can exchange data. A **LAN** (Local Area Network) covers one place, such as a home or an office. A **WAN** (Wide Area Network) connects places that are far apart, often through cables or links rented from a telephone company. The **internet** is the worldwide network of networks. Your own computer is also reachable by itself, through the special address `127.0.0.1`, called **localhost**. Every example in this topic uses it, so the server and the client both run on your machine.

| Network | Size | Example |
|---|---|---|
| LAN | One building or home | The Wi-Fi in a house |
| WAN | Cities or countries apart | A company's offices in two cities |
| Internet | The whole world | Every public website |

```python
import socket

print("localhost is", socket.gethostbyname("localhost"))
```

Output:

```
localhost is 127.0.0.1
```

## 2. The client-server model

Most network programs have two roles. The **server** waits for requests and answers them. The **client** starts the conversation by connecting to the server and sending a request. A web server is the server; your browser is the client. One server usually talks to many clients. In this lesson every example is a pair: one server script and one client script.

An everyday analogy: the server is a shop that is open all day, and clients are customers who walk in, ask for something, and leave.

## 3. IP address, port and protocol

To reach a program on another computer you need three things. The **IP address** identifies the computer, like a street address (`127.0.0.1`, `192.168.1.5`). The **port** is a number from 0 to 65535 that identifies one program on that computer, like a flat number inside a building. The **protocol** is the set of rules both sides follow so they understand each other, like the language they agree to speak.

Well-known services use fixed ports:

| Protocol | Port | Used for |
|---|---|---|
| HTTP | 80 | Web pages |
| HTTPS | 443 | Secure web pages |
| FTP | 21 | File transfer |
| SSH | 22 | Secure remote login |
| SMTP | 25 | Sending email |
| MySQL | 3306 | MySQL database server |

Ports below 1024 are reserved for such services, so our own programs use higher numbers. This lesson uses 5001 to 5005, a different port for each pair, so two examples never clash.

```python
import socket

# Python can look up well-known ports by protocol name.
for name in ["http", "https", "ssh", "smtp"]:
    print(f"{name:<6} port {socket.getservbyname(name)}")
```

Output:

```
http   port 80
https  port 443
ssh    port 22
smtp   port 25
```

## 4. TCP versus UDP

**TCP** (Transmission Control Protocol) makes a connection first, then delivers every byte in order and resends anything that gets lost. **UDP** (User Datagram Protocol) just sends packets; it is faster but packets can be lost or arrive out of order. Web pages, email and chat use TCP. Live video and online games often use UDP. All the examples here use TCP.

| | TCP | UDP |
|---|---|---|
| Connection | Connects first (like a phone call) | No connection (like posting letters) |
| Reliability | Every byte arrives, in order | Packets may be lost or reordered |
| Speed | Slower, more checking | Faster, less overhead |
| Socket type | `socket.SOCK_STREAM` | `socket.SOCK_DGRAM` |
| Used by | HTTP, email, file transfer | Video streaming, games, DNS |

## 5. What is a socket?

A **socket** is the end point of a network connection: the object your program uses to send and receive data. Both the client and the server create one. `socket.socket(socket.AF_INET, socket.SOCK_STREAM)` makes a socket for IPv4 addresses (`AF_INET`) and TCP (`SOCK_STREAM`). Use `with socket.socket(...) as s:` so the socket is closed automatically, like a file.

| Function | Who uses it | What it does |
|---|---|---|
| `socket()` | Both | Creates a socket |
| `bind((host, port))` | Server | Attaches the socket to an address and port |
| `listen()` | Server | Starts waiting for connections |
| `accept()` | Server | Blocks until a client connects; returns `(connection, address)` |
| `connect((host, port))` | Client | Connects to a server |
| `send(bytes)` | Both | Sends data; may send only part of it |
| `sendall(bytes)` | Both | Sends all the data; prefer this |
| `recv(size)` | Both | Receives up to `size` bytes; returns `b""` when the other side closed |
| `close()` | Both | Closes the socket (`with` does this for you) |

Sockets carry **bytes**, not strings. Call `.encode()` on a string before sending and `.decode()` on the received bytes to get a string back.

```python
import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Family:", s.family.name)
    print("Type:  ", s.type.name)

message = "hello"
as_bytes = message.encode()
print("Encoded:", as_bytes)
print("Decoded:", as_bytes.decode())
```

Output:

```
Family: AF_INET
Type:   SOCK_STREAM
Encoded: b'hello'
Decoded: hello
```

## 6. How to run the examples

Every example is a pair of scripts. Open two terminals in the `examples` folder. Start the server in the first terminal, then run the client in the second. The server waits (`accept()` blocks) until the client connects.

```
Terminal 1:  python 01_daytime_server.py
Terminal 2:  python 01_daytime_client.py
```

| Pair | Server | Client | Port |
|---|---|---|---|
| 01 | `01_daytime_server.py` | `01_daytime_client.py` | 5001 |
| 02 | `02_echo_server.py` | `02_echo_client.py` | 5002 |
| 03 | `03_welcome_server.py` | `03_welcome_client.py` | 5003 |
| 04 | `04_multi_client_server.py` | `04_multi_client_client.py` | 5004 |
| 05 | `05_chat_server.py` | `05_chat_client.py` | 5005 |

The servers in pairs 01, 02, 03 and 05 serve one client and then exit, so you can run them again right away. The server in pair 04 runs until you press Ctrl+C.

## 7. A daytime server and client

The server binds to `127.0.0.1:5001`, listens, accepts one client, sends the current time as bytes, and exits. The client connects, receives up to 1024 bytes, decodes them and prints the time. `setsockopt(... SO_REUSEADDR ...)` lets you restart a server immediately after it closes; without it some systems report "address already in use" for a minute.

Server (`examples/01_daytime_server.py`):

```python
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
```

Client (`examples/01_daytime_client.py`):

```python
import socket

HOST = "127.0.0.1"
PORT = 5001

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        data = client.recv(1024)                # up to 1024 bytes
        print("Server time:", data.decode())    # bytes back to text
except ConnectionRefusedError:
    print(f"Could not connect to {HOST}:{PORT}. Is the server running?")
```

Output in terminal 1 (server; the client's port number and the time will differ):

```
Daytime server listening on 127.0.0.1:5001 ...
Client connected from ('127.0.0.1', 3348)
Sent: 2026-10-29 16:33:16
Server finished.
```

Output in terminal 2 (client):

```
Server time: 2026-10-29 16:33:16
```

## 8. An echo server and client

An echo server sends back whatever it receives. The server loops: `recv()` a message, `sendall()` it back. When the client closes its socket, `recv()` returns empty bytes (`b""`), and the loop ends. The client reads lines from the keyboard until you type `quit`.

Server (`examples/02_echo_server.py`):

```python
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
```

Client (`examples/02_echo_client.py`):

```python
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
```

Client session (what you type is shown after `You:`):

```
Connected. Type quit to stop.
You: hello
Echo: hello
You: Python is fun
Echo: Python is fun
You: quit
Disconnected.
```

Server output:

```
Echo server listening on 127.0.0.1:5002 ...
Client connected from ('127.0.0.1', 3349)
Received: hello
Received: Python is fun
Client left. Server finished.
```

## 9. A welcome server and client

Here the client sends data first: its name. The server receives the name, builds a greeting and sends it back. This is the usual request-and-response pattern: the client asks, the server answers.

Server (`examples/03_welcome_server.py`):

```python
import socket

HOST = "127.0.0.1"
PORT = 5003

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Welcome server listening on {HOST}:{PORT} ...")

    connection, address = server.accept()
    with connection:
        name = connection.recv(1024).decode().strip()
        print(f"{name} connected from {address}")
        greeting = f"Welcome, {name}! Nice to meet you."
        connection.sendall(greeting.encode())

print("Server finished.")
```

Client (`examples/03_welcome_client.py`):

```python
import socket

HOST = "127.0.0.1"
PORT = 5003

name = input("Your name: ")

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        client.sendall(name.encode())
        reply = client.recv(1024)
        print("Server says:", reply.decode())
except ConnectionRefusedError:
    print(f"Could not connect to {HOST}:{PORT}. Is the server running?")
```

Client session:

```
Your name: Sita
Server says: Welcome, Sita! Nice to meet you.
```

Server output:

```
Welcome server listening on 127.0.0.1:5003 ...
Sita connected from ('127.0.0.1', 3350)
Server finished.
```

## 10. A multi-client server with threads

The servers above serve one client at a time. To serve several clients at once, the server starts a new thread for every accepted connection (see the Multithreading topic). The main thread only accepts connections; each worker thread talks to its own client. This server loops forever; stop it with Ctrl+C in its terminal. The one-second timeout on `accept()` makes the loop wake up regularly so Ctrl+C is noticed on every operating system.

Server (`examples/04_multi_client_server.py`):

```python
import socket
import threading

HOST = "127.0.0.1"
PORT = 5004


def handle_client(connection, address):
    thread_name = threading.current_thread().name
    print(f"[{thread_name}] connected: {address}")
    with connection:
        while True:
            data = connection.recv(1024)
            if not data:
                break
            message = data.decode()
            print(f"[{thread_name}] received: {message}")
            connection.sendall(f"{thread_name} got: {message}".encode())
    print(f"[{thread_name}] disconnected: {address}")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    # accept() would block forever; a one-second timeout lets the loop
    # wake up regularly so Ctrl+C is noticed on every operating system.
    server.settimeout(1.0)
    print(f"Server listening on {HOST}:{PORT}. Press Ctrl+C to stop.")

    client_count = 0
    try:
        while True:
            try:
                connection, address = server.accept()
            except TimeoutError:
                continue                        # nobody connected; check again
            client_count += 1
            worker = threading.Thread(
                target=handle_client,
                args=(connection, address),
                name=f"Client-{client_count}",
                daemon=True,
            )
            worker.start()
    except KeyboardInterrupt:
        print("\nServer stopped.")
```

Client (`examples/04_multi_client_client.py`), run it in two terminals at the same time:

```python
import socket
import time

HOST = "127.0.0.1"
PORT = 5004
MESSAGES = ["hello", "how are you", "goodbye"]

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        for message in MESSAGES:
            client.sendall(message.encode())
            reply = client.recv(1024)
            print("Server:", reply.decode())
            time.sleep(0.5)     # stay connected a moment so clients overlap
    print("Done.")
except ConnectionRefusedError:
    print(f"Could not connect to {HOST}:{PORT}. Is the server running?")
```

Server output with two clients connected at the same time (the order of the lines depends on timing):

```
Server listening on 127.0.0.1:5004. Press Ctrl+C to stop.
[Client-1] connected: ('127.0.0.1', 6582)
[Client-1] received: hello
[Client-2] connected: ('127.0.0.1', 6583)
[Client-2] received: hello
[Client-1] received: how are you
[Client-2] received: how are you
[Client-1] received: goodbye
[Client-2] received: goodbye
[Client-1] disconnected: ('127.0.0.1', 6582)
[Client-2] disconnected: ('127.0.0.1', 6583)
```

Each client prints:

```
Server: Client-1 got: hello
Server: Client-1 got: how are you
Server: Client-1 got: goodbye
Done.
```

## 11. A two-way chat

In a chat, both sides send and receive. This simple version takes turns: the client sends a line, the server reads it and types a reply, the client reads the reply, and so on. The chat ends when either side types `bye`. Whoever receives `bye` stops too.

Server (`examples/05_chat_server.py`):

```python
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
```

Client (`examples/05_chat_client.py`):

```python
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
```

Client session:

```
Connected. Type bye to end the chat.
You: hello
Server: hi there
You: how are you
Server: fine thanks
You: bye
You ended the chat.
```

Server session:

```
Chat server listening on 127.0.0.1:5005 ...
Client connected. Waiting for the first message.
Client: hello
You: hi there
Client: how are you
You: fine thanks
Client: bye
Client said bye. Chat over.
```

## 12. Handling ConnectionRefusedError

If the client runs while no server is listening on that port, `connect()` raises `ConnectionRefusedError`. Every client in this topic catches it and prints a helpful message instead of a traceback. Run any client without its server to see it.

```python
import socket

HOST = "127.0.0.1"
PORT = 5001

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        print("Connected.")
except ConnectionRefusedError:
    print(f"Could not connect to {HOST}:{PORT}. Is the server running?")
```

Output (no server running):

```
Could not connect to 127.0.0.1:5001. Is the server running?
```

## Common mistakes

- `OSError: [Errno 98] Address already in use` (or `WinError 10048`) -> another program, or a previous run of your server, still holds the port. Stop it, wait a moment, or choose another port; `SO_REUSEADDR` helps after a clean close.
- `ConnectionRefusedError` -> the server is not running, or the client uses a different host or port. Start the server first and check both scripts use the same `PORT`.
- `TypeError: a bytes-like object is required, not 'str'` -> you passed a string to `sendall()`. Use `message.encode()` before sending and `data.decode()` after receiving.
- The client hangs forever -> both sides are waiting in `recv()`. Decide who speaks first and make sure every `recv()` has a matching `sendall()` on the other side.
- Running the client before the server -> the server must be listening before the client connects. Start the server in its own terminal first.
- Forgetting to close sockets -> use `with socket.socket(...) as s:` and `with connection:` so they close automatically.

## Summary

- A network connects computers; the internet is the network of networks; `127.0.0.1` is your own computer.
- A server waits for requests; a client connects and asks. IP address = which computer, port = which program, protocol = the rules.
- TCP is reliable and ordered (`SOCK_STREAM`); UDP is fast but may lose packets (`SOCK_DGRAM`).
- Server steps: `socket`, `bind`, `listen`, `accept`, then `recv`/`sendall`, `close`. Client steps: `socket`, `connect`, `sendall`/`recv`, `close`.
- Sockets carry bytes: `encode()` before sending, `decode()` after receiving.
- `recv()` returns `b""` when the other side has closed the connection.
- One thread per client lets a server talk to many clients at the same time.
- Catch `ConnectionRefusedError` so a missing server gives a clear message.

## Exercises

Practice what you learned in [exercises/README.md](exercises/README.md).

---

[Previous: Multithreading](../15-multithreading/README.md) | [Next: Databases](../17-databases/README.md) | [Home](../README.md)
