def is_prime(num):
    """Return True if num is a prime number, otherwise False."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):  # check only up to sqrt(num)
        if num % i == 0:
            return False
    return True


def prime_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes


print(is_prime(11))
print(prime_in_range(10, 50))
