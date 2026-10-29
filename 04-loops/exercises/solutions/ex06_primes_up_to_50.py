"""Print every prime number from 2 to 50 on one line."""

for candidate in range(2, 51):
    # Look for a divisor. The first one found means "not prime": break.
    for divisor in range(2, candidate):
        if candidate % divisor == 0:
            break
    else:
        # No break happened, so no divisor was found.
        print(candidate, end=" ")
print()
