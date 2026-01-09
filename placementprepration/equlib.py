import sys


def leaders(arr):
    n = len(arr)
    result = []
    for i in range(n):
        if all(arr[i] >= arr[j] for j in range(i + 1, n)):
            result.append(arr[i])
    return result


def max_leader(arr):
    if not arr:
        return 0
    return max(arr)


def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    n, *rest = data
    arr = rest[:n]
    l = leaders(arr)
    res = max_leader(l)
    print(res)


if __name__ == "__main__":
    main()
