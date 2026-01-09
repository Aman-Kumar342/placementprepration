import sys


def max_sliding(arr, k):
    n = len(arr)
    if k == 0 or k > n:
        return []
    res = []
    for i in range(n - k + 1):
        res.append(max(arr[i : i + k]))
    return res


def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if len(data) < 2:
        return
    n, k, *rest = data
    arr = rest[:n]
    res = max_sliding(arr, k)
    print(" ".join(map(str, res)))


if __name__ == "__main__":
    main()
