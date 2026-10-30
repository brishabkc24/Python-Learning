"""Write missing_rules(password) that lists which strength rules a password fails."""

import re

RULES = [
    ("length 8-16", r"^.{8,16}$"),
    ("uppercase", r"[A-Z]"),
    ("lowercase", r"[a-z]"),
    ("digit", r"\d"),
    ("special character", r"[!@#$%^&*]"),
]


def missing_rules(password):
    return [name for name, pattern in RULES if not re.search(pattern, password)]


for password in ["Strong@123", "weak", "NoDigits!", "alllower123"]:
    missing = missing_rules(password)
    if missing:
        print(f"{password} -> missing: {', '.join(missing)}")
    else:
        print(f"{password} -> strong")
