import sys
from collections import deque


def first_negatives(arr, k):
    q = deque()
    res = []
    for i, val in enumerate(arr):
        if val < 0:
            q.append(i)
        if i >= k - 1:
            while q and q[0] < i - k + 1:
                q.popleft()
            res.append(arr[q[0]] if q else 0)
    return res


def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if len(data) < 2:
        return
    n, k, *rest = data
    arr = rest[:n]
    res = first_negatives(arr, k)
    print(" ".join(map(str, res)))


if __name__ == "__main__":
    main()
