"""Show the five types of inheritance and the method resolution order.

Single, multilevel, multiple, hierarchical and hybrid inheritance each
get a tiny class tree. The end prints __mro__ to show the order in
which Python searches for a method. Run: python 02_types_of_inheritance.py
"""


# Single: one parent, one child
class Device:
    def power_on(self):
        return "powered on"


class Phone(Device):
    pass


# Multilevel: a chain of three
class Smartphone(Phone):
    def browse(self):
        return "browsing the web"


# Multiple: one child, two parents
class Camera:
    def take_photo(self):
        return "photo taken"


class CameraPhone(Phone, Camera):
    pass


# Hierarchical: one parent, several children
class Tablet(Device):
    pass


class Laptop(Device):
    pass


# Hybrid: a mix (hierarchical Device -> Tablet/Laptop, then multiple)
class Convertible(Tablet, Laptop):
    pass


print("Single      :", Phone().power_on())
print("Multilevel  :", Smartphone().power_on(), "and", Smartphone().browse())
print("Multiple    :", CameraPhone().power_on(), "and", CameraPhone().take_photo())
print("Hierarchical:", Tablet().power_on(), "/", Laptop().power_on())
print("Hybrid      :", Convertible().power_on())

print("\nMethod resolution order (the search path for a method):")
for cls in (Smartphone, CameraPhone, Convertible):
    path = " -> ".join(parent.__name__ for parent in cls.__mro__)
    print(f"  {cls.__name__:<12} {path}")
