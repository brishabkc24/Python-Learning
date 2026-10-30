"""A bank account shared by two threads: withdraw without and with a lock.

Run: python 07_bank_account_lock.py
Two people try to withdraw 80 from an account holding 100. Without a
lock both see "enough money" at the same moment and the balance goes
negative. With a lock the second withdrawal is refused.
"""

import threading
import time


class BankAccount:
    def __init__(self, owner, balance, use_lock):
        self.owner = owner
        self.balance = balance
        self.use_lock = use_lock
        self.lock = threading.Lock()

    def withdraw(self, amount):
        if self.use_lock:
            with self.lock:
                self._do_withdraw(amount)
        else:
            self._do_withdraw(amount)

    def _do_withdraw(self, amount):
        name = threading.current_thread().name
        if self.balance >= amount:
            time.sleep(0.1)     # the bank "processes" the request
            self.balance -= amount
            print(f"{name}: withdrew {amount}, balance is now {self.balance}")
        else:
            print(f"{name}: not enough money for {amount}, balance is {self.balance}")


def try_both(account):
    thread_a = threading.Thread(target=account.withdraw, args=(80,), name="Aarav")
    thread_b = threading.Thread(target=account.withdraw, args=(80,), name="Sita")
    thread_a.start()
    thread_b.start()
    thread_a.join()
    thread_b.join()
    print(f"Final balance: {account.balance}")


print("--- Without a lock ---")
try_both(BankAccount("Shared", 100, use_lock=False))

print()
print("--- With a lock ---")
try_both(BankAccount("Shared", 100, use_lock=True))
