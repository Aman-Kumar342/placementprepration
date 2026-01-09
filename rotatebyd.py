import sys


def rotate_left(arr, d):
    n = len(arr)
    if n == 0:
        return arr
    d %= n
    return arr[d:] + arr[:d]


def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if len(data) < 2:
        return
    n, *rest = data
    arr = rest[:n]
    if len(rest) > n:
        d = rest[n]
    else:
        d = 0
    rotated = rotate_left(arr, d)
    print(" ".join(map(str, rotated)))


if __name__ == "__main__":
    main()
