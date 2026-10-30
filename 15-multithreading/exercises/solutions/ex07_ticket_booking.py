"""Let five customer threads book from three remaining seats, using a Lock so that exactly three bookings succeed."""

import threading
import time


class TicketCounter:
    def __init__(self, seats):
        self.seats = seats
        self.lock = threading.Lock()

    def book(self, customer):
        with self.lock:
            if self.seats > 0:
                time.sleep(0.05)        # printing the ticket takes a moment
                self.seats -= 1
                print(f"{customer}: booked, seats left: {self.seats}")
            else:
                print(f"{customer}: sorry, sold out")


counter = TicketCounter(seats=3)
customers = ["Aarav", "Sita", "Bikash", "Priya", "Rohan"]

threads = [threading.Thread(target=counter.book, args=(name,)) for name in customers]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print("Seats left at the end:", counter.seats)
