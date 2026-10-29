"""
Local and global scope: which variables a function can see, what the
global keyword does, and the cleaner alternative of passing and returning
values.

Run: python 04_scope.py
"""

balance = 1000  # a global variable, visible everywhere in this file


def show_balance():
    # A function can read a global variable without any special keyword.
    currency = "NPR"  # a local variable, visible only inside this function
    print("Balance:", balance, currency)


show_balance()

# The local variable does not exist out here.
print("Is 'currency' defined outside the function?", "currency" in dir())


def deposit_with_global(amount):
    # global tells Python to change the module-level variable.
    # This works, but it hides the change from whoever reads the call.
    global balance
    balance = balance + amount


deposit_with_global(500)
print("After deposit_with_global(500):", balance)


def deposit(current_balance, amount):
    # Preferred style: take the value in, give the new value back.
    # Nothing outside the function changes by surprise.
    return current_balance + amount


balance = deposit(balance, 250)
print("After balance = deposit(balance, 250):", balance)


def shadow_example():
    # Assigning inside a function makes a NEW local variable.
    # The global 'balance' is untouched.
    balance = 0
    print("Inside shadow_example, balance is", balance)


shadow_example()
print("Outside, balance is still", balance)
