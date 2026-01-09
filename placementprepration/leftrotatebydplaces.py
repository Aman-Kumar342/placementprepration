import sys


def rotate_left(arr, k):
    n = len(arr)
    if n == 0:
        return arr
    k %= n
    return arr[k:] + arr[:k]


def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if len(data) < 2:
        return
    n, k, *rest = data
    arr = rest[:n]
    rotated = rotate_left(arr, k)
    print(" ".join(map(str, rotated)))


if __name__ == "__main__":
    main()
