import math


def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def get_primes(limit):
    """Return a list of prime numbers up to a given limit."""
    primes = []
    for num in range(limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes


if __name__ == "__main__":
    print(get_primes(50))
