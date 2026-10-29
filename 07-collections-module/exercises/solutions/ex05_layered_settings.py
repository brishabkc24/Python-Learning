"""Exercise 5: layered settings with ChainMap, where the first dictionary wins and receives writes."""

from collections import ChainMap

command_line = {}
environment = {"debug": "yes"}
defaults = {"debug": "no", "port": 8000, "host": "localhost"}

settings = ChainMap(command_line, environment, defaults)

print("debug:", settings["debug"])
print("port:", settings["port"])
print("host:", settings["host"])

settings["port"] = 9000
print("command line now:", command_line)
print("defaults still:", defaults)
