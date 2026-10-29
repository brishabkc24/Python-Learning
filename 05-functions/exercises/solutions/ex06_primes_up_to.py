"""Exercise 6: is_prime helper and primes_up_to that lists every prime up to a limit."""


def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True


def primes_up_to(limit):
    primes = []
    for candidate in range(2, limit + 1):
        if is_prime(candidate):
            primes.append(candidate)
    return primes


primes = primes_up_to(50)
print("Primes up to 50:", primes)
print("Count:", len(primes))
