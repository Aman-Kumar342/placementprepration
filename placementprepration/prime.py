import sys


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def print_primes(limit):
    primes = [str(i) for i in range(2, limit + 1) if is_prime(i)]
    if primes:
        print(" ".join(primes))


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    limit = int(data[0])
    print_primes(limit)


if __name__ == "__main__":
    main()
