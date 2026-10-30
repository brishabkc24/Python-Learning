# Chat App

## What it does

A small group chat for one computer. `server.py` waits for connections on `127.0.0.1`, port `5050`. Any number of `client.py` programs can connect, each with a name. Every line a client types is sent to the server, which passes it on to all the other clients with the sender's name in front, for example `Bikash: hello everyone`. Joining and leaving are announced. Typing `bye` leaves the chat.

## Concepts used

- The `socket` module: `bind`, `listen`, `accept` on the server and `create_connection` on the client
- One thread per client on the server (`threading.Thread` with `daemon=True`) so many clients are served at once
- A `threading.Lock` around the shared dictionary of connected clients
- A background thread in the client that prints incoming messages while the main thread waits for your typing
- `socket.makefile("r")` to read the connection line by line, exactly like a file
- A timeout on `accept()` so Ctrl+C stops the server on every operating system
- `sys.argv` for an optional name on the command line

## Files

| File | Purpose |
|---|---|
| `server.py` | the server; start it first and leave it running |
| `client.py` | one chat participant; run it once per person |

## How to run

You need three terminals (or more). Open each one in this folder.

Terminal 1, the server:

```
cd 19-projects/chat-app
python server.py
```

Terminal 2, the first client:

```
cd 19-projects/chat-app
python client.py Asha
```

Terminal 3, the second client:

```
cd 19-projects/chat-app
python client.py Bikash
```

Now type in terminal 2 or 3. Each line appears in the other client's terminal with the sender's name, and in the server terminal too. Type `bye` to leave. Press Ctrl+C in terminal 1 to stop the server. If you run `client.py` without a name it asks for one.

## Sample session

Terminal 1 (server):

```
Chat server listening on 127.0.0.1:5050. Press Ctrl+C to stop.
*** Asha joined the chat (127.0.0.1:11807)
*** Bikash joined the chat (127.0.0.1:11808)
Bikash: hello everyone
Asha: hi Bikash
*** Bikash left the chat
*** Asha left the chat
```

Terminal 2 (Asha):

```
Welcome, Asha! Type bye to leave.
*** Bikash joined the chat (127.0.0.1:11808)
Bikash: hello everyone
hi Bikash
*** Bikash left the chat
bye
Disconnected from the server.
```

Terminal 3 (Bikash):

```
Welcome, Bikash! Type bye to leave.
hello everyone
Asha: hi Bikash
bye
Disconnected from the server.
```

The lines without a name in front are the ones that person typed. The port numbers after the address differ on every run.

## Ideas to extend it

- Add a `/list` command that shows who is connected.
- Add private messages with `/msg Name text`.
- Save the conversation to a log file on the server.

---

[Back to the project index](../README.md)
