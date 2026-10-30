"""Force child classes to implement required methods with abc.ABC.

Notification is abstract: it cannot be instantiated, and every child
must implement send(). A child that forgets a method is also refused.
Run: python 06_abstraction_abc.py
"""

from abc import ABC, abstractmethod


class Notification(ABC):
    def __init__(self, recipient):
        self.recipient = recipient

    @abstractmethod
    def send(self, message):
        """Deliver the message. Every child must write its own version."""

    def send_many(self, messages):
        # A normal method: shared logic that relies on the abstract send().
        for message in messages:
            self.send(message)


class EmailNotification(Notification):
    def send(self, message):
        print(f"Email to {self.recipient}: {message}")


class SmsNotification(Notification):
    def send(self, message):
        print(f"SMS to {self.recipient}: {message}")


class PushNotification(Notification):
    def send(self, message):
        print(f"Push to device {self.recipient}: {message}")


class BrokenNotification(Notification):
    pass                                   # forgot to implement send()


channels = [
    EmailNotification("asha@example.com"),
    SmsNotification("9800000001"),
    PushNotification("device-42"),
]
for channel in channels:
    channel.send("Your order has shipped")

print("\nsend_many() is inherited and uses each child's send():")
channels[0].send_many(["Welcome!", "Your password was changed"])

print("\nAbstract classes cannot be instantiated:")
try:
    Notification("nobody@example.com")
except TypeError as error:
    print("Error:", error)

print("\nA child that forgets an abstract method cannot be instantiated either:")
try:
    BrokenNotification("nobody@example.com")
except TypeError as error:
    print("Error:", error)
