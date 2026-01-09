import sys


def find_leaders(arr):
    best = -2147483648
    res = []
    for value in reversed(arr):
        if value > best:
            res.append(value)
            best = value
    return list(reversed(res))


def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    n, *rest = data
    arr = rest[:n]
    res = find_leaders(arr)
    print(res)


if __name__ == "__main__":
    main()
