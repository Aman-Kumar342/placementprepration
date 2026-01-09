import sys


def rotate_left_by_one(arr):
    if not arr:
        return arr
    return arr[1:] + arr[:1]


def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    n, *rest = data
    arr = rest[:n]
    rotated = rotate_left_by_one(arr)
    print(" ".join(map(str, rotated)))


if __name__ == "__main__":
    main()
