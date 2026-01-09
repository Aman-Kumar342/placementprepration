import sys
import math


def combination(n, r):
    if r < 0 or r > n:
        return None
    return math.comb(n, r)


def main():
    data = sys.stdin.read().strip().split()
    if len(data) < 2:
        return
    n, r = map(int, data[:2])
    result = combination(n, r)
    if result is None:
        print("Invalid input")
    else:
        print(result)


if __name__ == "__main__":
    main()
