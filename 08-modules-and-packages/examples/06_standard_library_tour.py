"""
A quick tour of eight standard library modules: math, random, datetime,
time, os, sys, statistics and json, with one or two lines each. The
random numbers are seeded so they repeat; the date and folder lines
depend on when and where you run the script.

Run: python 06_standard_library_tour.py
"""

import datetime
import json
import math
import os
import random
import statistics
import sys
import time

print("math:       sqrt(81) =", math.sqrt(81), "| 2**10 =", math.pow(2, 10), "| gcd =", math.gcd(24, 36))

random.seed(1)
print("random:     dice =", random.randint(1, 6), "| pick =", random.choice(["tea", "coffee"]),
      "| sample =", random.sample(range(1, 20), 3))

print("datetime:   today =", datetime.date.today(), "| exam =", datetime.date(2026, 3, 15).strftime("%A %d %B"))
print("datetime:   in 45 days =", datetime.date(2026, 3, 15) + datetime.timedelta(days=45))

start = time.perf_counter()
time.sleep(0.1)
print("time:       slept", round(time.perf_counter() - start, 1), "s | year from timestamp =",
      time.localtime().tm_year)

print("os:         folder =", os.path.basename(os.getcwd()), "| os name =", os.name,
      "| this file exists =", os.path.exists(__file__))

print("sys:        version =", sys.version_info.major, sys.version_info.minor,
      "| arguments =", sys.argv[1:], "| platform =", sys.platform)

marks = [67, 92, 45, 85, 92, 73]
print("statistics: mean =", round(statistics.mean(marks), 1), "| median =", statistics.median(marks),
      "| mode =", statistics.mode(marks), "| stdev =", round(statistics.stdev(marks), 1))

student = {"name": "Sita", "marks": marks[:2], "passed": True}
as_text = json.dumps(student)
print("json:       text =", as_text)
print("json:       back to data =", json.loads(as_text)["name"], "(files: see File Handling)")
