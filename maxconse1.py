import sys


def max_consecutive_ones(arr):
    count = 0
    best = 0
    for val in arr:
        if val == 1:
            count += 1
            best = max(best, count)
        else:
            count = 0
    return best


def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    n, *rest = data
    arr = rest[:n]
    print(max_consecutive_ones(arr))


if __name__ == "__main__":
    main()
