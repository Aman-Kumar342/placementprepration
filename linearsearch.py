import sys


def linear_search(arr, target):
    for idx, value in enumerate(arr):
        if value == target:
            return idx
    return -1


def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    if len(data) < 2:
        print(-1)
        return
    n, target, *rest = data
    arr = rest[:n]
    result = linear_search(arr, target)
    print(result)


if __name__ == "__main__":
    main()
