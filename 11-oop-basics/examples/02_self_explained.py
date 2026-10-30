"""Show what self means and when __init__ runs.

A print() inside __init__ proves it runs automatically at creation.
The long form Dog.bark(buddy) shows that self is simply the object
on the left of the dot. Run: python 02_self_explained.py
"""


class Dog:
    def __init__(self, name, sound="Woof"):
        print(f"  (__init__ is running, self is the new object for {name})")
        self.name = name
        self.sound = sound

    def bark(self, times=1):
        # self.name reads the data of whichever dog called bark()
        words = " ".join([self.sound] * times)
        print(f"{self.name} says {words}")

    def rename(self, new_name):
        print(f"Renaming {self.name} to {new_name}")
        self.name = new_name


print("Creating buddy:")
buddy = Dog("Buddy")
print("Creating rex:")
rex = Dog("Rex", "Grrr")

print("\nCalling methods the normal way:")
buddy.bark()          # Python passes buddy as self
rex.bark(times=3)     # Python passes rex as self

print("\nThe long form does the same thing:")
Dog.bark(buddy)       # self is given explicitly

print("\nA method can change the object it was called on:")
buddy.rename("Max")
buddy.bark()
print("rex is unchanged:", rex.name)
