"""Show a working... message from a daemon thread while the main thread processes three items."""

import threading
import time


def show_progress():
    while True:
        print("working...")
        time.sleep(0.2)


progress_thread = threading.Thread(target=show_progress, daemon=True)
progress_thread.start()

for item in ["item 1", "item 2", "item 3"]:
    time.sleep(0.3)
    print(f"Processed {item}")

# The daemon thread is still looping, but the program ends here anyway.
print("Main thread finished")
