"""Simulate downloading several files one by one and then all at once.

Run: python 05_download_simulation.py
Each "download" only sleeps, which stands for waiting on the network.
Threads shine here: while one thread waits, the others can wait too,
so the total time is close to the slowest file, not the sum of all.
The order of the "finished" lines can differ between runs.
"""

import threading
import time

# (file name, size in MB); the fake speed is 10 MB per second.
FILES = [("photo.jpg", 3), ("song.mp3", 5), ("notes.txt", 2), ("video.mp4", 4)]
SPEED_MB_PER_SECOND = 10


def download(file_name, size_mb):
    print(f"Starting  {file_name} ({size_mb} MB)")
    time.sleep(size_mb / SPEED_MB_PER_SECOND)
    print(f"Finished  {file_name}")


print("--- One file after another ---")
start_time = time.perf_counter()
for file_name, size_mb in FILES:
    download(file_name, size_mb)
print(f"Sequential time: {time.perf_counter() - start_time:.1f} s")

print()
print("--- All files at the same time ---")
start_time = time.perf_counter()
threads = []
for file_name, size_mb in FILES:
    thread = threading.Thread(target=download, args=(file_name, size_mb))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
print(f"Threaded time:   {time.perf_counter() - start_time:.1f} s")
