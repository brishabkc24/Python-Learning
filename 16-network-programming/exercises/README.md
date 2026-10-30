# Network Programming: Exercises

Solutions are in the [solutions](solutions/) folder. Try each exercise yourself before looking.

For exercises 2 to 6 you may write the server and the client as two separate scripts and run them in two terminals, exactly like the examples. The solution files take a shortcut so that each one runs from a single command: the server runs in a background thread (from the Multithreading topic) and the client runs in the main thread of the same file. Use ports 5006 to 5010, one per exercise, so nothing clashes with the examples.

## 1. Ports and addresses

**No sockets yet.** Write a function `is_valid_ipv4(text)` that returns `True` when `text` is four numbers from 0 to 255 separated by dots, and `False` otherwise. Then store the well-known ports for HTTP, HTTPS, FTP, SSH, SMTP and MySQL in a dictionary, print them sorted by port number, and look up `HTTPS` and `Telnet` (which is not in the table).

Example:

```
127.0.0.1       valid: True
192.168.1.300   valid: False
10.0.0          valid: False
8.8.8.8         valid: True
abc.def.1.2     valid: False

FTP    -> port 21
SSH    -> port 22
SMTP   -> port 25
HTTP   -> port 80
HTTPS  -> port 443
MySQL  -> port 3306

HTTPS: 443
Telnet: not in the table
```

## 2. Uppercase server

**One request, one reply.** Write a server on port 5006 that accepts one client, receives a sentence, and sends it back in upper case. Write a client that sends `python makes networking simple` and prints the reply.

Example:

```
Server received: python makes networking simple
Client got:      PYTHON MAKES NETWORKING SIMPLE
```

## 3. Calculator server

**Many requests on one connection.** Write a server on port 5007 that keeps receiving requests of the form `add 2 3`, `sub 5 1`, `mul 4 2.5` or `div 7 0` and replies with the result, or with an error message for division by zero or an unknown operation. The connection ends when the client sends `quit`. The client sends a list of requests and prints each request with its reply.

Example:

```
add 2 3 -> 5.0
mul 4 2.5 -> 10.0
div 7 0 -> error: division by zero
pow 2 3 -> error: unknown operation pow
Client: quit
```

## 4. Guess the number

**A small game protocol.** The server on port 5008 holds a secret number (42). For every guess the client sends, the server replies `too high`, `too low` or `correct`, and closes after `correct`. The client sends the guesses 50, 25, 37, 43 and 42 one by one, prints each reply, and stops when it hears `correct`.

Example:

```
Guess 1: 50 -> too high
Guess 2: 25 -> too low
Guess 3: 37 -> too low
Guess 4: 43 -> too high
Guess 5: 42 -> correct
Found the number in 5 guesses.
```

## 5. Visitor counter

**One thread per client.** Write a server on port 5009 that starts a new thread for every client and sends `You are visitor number N`, where N counts the clients so far. Protect the counter with a lock. Connect three clients named Aarav, Sita and Bikash at the same time (three client threads) and print what each one receives, then the total.

Example (the order of the first three lines may vary):

```
Aarav got: You are visitor number 1
Sita got: You are visitor number 2
Bikash got: You are visitor number 3
Total visitors: 3
```

## 6. Retry until the server is up

**Handling ConnectionRefusedError.** Write a client for port 5010 that tries to connect up to five times. After each `ConnectionRefusedError` it prints `Attempt N: server not available, retrying in 1 s` and waits one second. When it connects it prints the server's message. To test it, start the server a few seconds late (in the solution the server thread sleeps 3.5 seconds before listening). The number of failed attempts you see depends on your operating system, because some systems keep trying a refused port for a second or two before giving up.

Example:

```
Attempt 1: server not available, retrying in 1 s
Attempt 2: connected
Server says: Thanks for waiting!
```
