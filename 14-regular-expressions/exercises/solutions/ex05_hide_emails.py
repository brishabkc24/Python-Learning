"""Replace every email address in a sentence with [hidden] and report the count."""

import re

message = "Write to asha@example.com or support@example.org today"

hidden, count = re.subn(r"[\w.]+@[\w.]+\.[a-z]{2,}", "[hidden]", message)
print(hidden)
print(count, "addresses hidden")
