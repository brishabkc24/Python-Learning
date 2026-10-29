"""Decide whether a person may vote: they must be a citizen and at least 18.
Shows the same rule written with a nested if and with the and operator.

Run: python 02_vote_eligibility.py
"""

# Version 1: a nested if. The inner if is only reached when the outer
# condition is True, so this reads as "first check citizenship, then age".
name = "Asha"
age = 20
is_citizen = True

print(f"Checking {name}, age {age}, citizen = {is_citizen}")
if is_citizen:
    if age >= 18:
        print("  Eligible to vote.")
    else:
        print("  Not eligible: under 18.")
else:
    print("  Not eligible: not a citizen.")

print()

# Version 2: the and operator. Both conditions must be True.
# It is shorter, but it cannot tell the person which test failed.
name = "Ravi"
age = 16
is_citizen = True

print(f"Checking {name}, age {age}, citizen = {is_citizen}")
if is_citizen and age >= 18:
    print("  Eligible to vote.")
else:
    print("  Not eligible.")

print()

# Version 3: give the exact reason with elif. The first True branch wins,
# so the "eligible" case is tested first and the reasons come afterwards.
name = "Meera"
age = 30
is_citizen = False

print(f"Checking {name}, age {age}, citizen = {is_citizen}")
if is_citizen and age >= 18:
    print("  Eligible to vote.")
elif not is_citizen:
    print("  Not eligible: not a citizen.")
else:
    print("  Not eligible: under 18.")
