import sys


def max_equilibrium_sum(arr):
    total = sum(arr)
    left = 0
    best = None
    for value in arr:
        total -= value
        if left == total:
            best = left if best is None else max(best, left)
        left += value
    return best


def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    n, *rest = data
    arr = rest[:n]
    best = max_equilibrium_sum(arr)
    if best is None:
        print(-2147483648)
    else:
        print(best)


if __name__ == "__main__":
    main()
