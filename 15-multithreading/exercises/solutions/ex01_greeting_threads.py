"""Create three named threads that each print a greeting with their own name, then print All done."""

import threading


def say_hello():
    print(f"Hello from {threading.current_thread().name}")


threads = []
for number in range(1, 4):
    thread = threading.Thread(target=say_hello, name=f"Worker-{number}")
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All done")
