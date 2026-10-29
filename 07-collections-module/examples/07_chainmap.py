"""
ChainMap: combine several dictionaries into one view with a clear lookup
order, used here for program settings (command line, then user file,
then built-in defaults).

Run: python 07_chainmap.py
"""

from collections import ChainMap

defaults = {"theme": "light", "language": "en", "font_size": 12, "autosave": True}
user_file = {"theme": "dark", "font_size": 14}
command_line = {"font_size": 18}

# The first dictionary wins; later ones fill in what is missing.
settings = ChainMap(command_line, user_file, defaults)

for key in ["theme", "language", "font_size", "autosave"]:
    print(key.ljust(10), "->", settings[key])

print()
print("number of keys:", len(settings))
print("all keys:", sorted(settings))
print("maps in order:", settings.maps)

print()
# Writing through the ChainMap changes only the first dictionary.
settings["language"] = "ne"
print("command_line now:", command_line)
print("defaults unchanged:", defaults)

# The dictionaries are not copied, so changing one shows through.
user_file["theme"] = "blue"
print("theme after editing user_file:", settings["theme"])

print()
# new_child() adds a fresh, empty dictionary in front for temporary changes.
session = settings.new_child()
session["theme"] = "high-contrast"
print("session theme:", session["theme"])
print("settings theme is still:", settings["theme"])

# Finding which dictionary a key came from.
for mapping in settings.maps:
    if "autosave" in mapping:
        print("'autosave' came from:", mapping)
        break
