import sys


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if len(data) < 2:
        return
    a, b = data[:2]
    print(gcd(a, b))


if __name__ == "__main__":
    main()
