import sys
from collections import Counter


def find_single(nums):
    counts = Counter(nums)
    for value, freq in counts.items():
        if freq == 1:
            return value
    return -1


def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    n, *rest = data
    arr = rest[:n]
    print(find_single(arr))


if __name__ == "__main__":
    main()
