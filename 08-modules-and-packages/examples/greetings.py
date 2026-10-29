"""
A tiny module with two greeting functions, used by 02_use_greetings.py
and 03_name_main_demo.py to show how importing your own file works.

Run directly to see its self-test: python greetings.py
"""

DEFAULT_NAME = "friend"


def hello(name=DEFAULT_NAME):
    """Return a greeting for the given name."""
    return "Hello, " + name + "!"


def goodbye(name=DEFAULT_NAME):
    """Return a farewell for the given name."""
    return "Goodbye, " + name + "."


if __name__ == "__main__":
    print(hello("tester"))
    print(goodbye("tester"))
