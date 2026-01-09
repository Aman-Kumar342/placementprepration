import sys


def move_zero_to_end(arr):
    nz = [x for x in arr if x != 0]
    zeros = [0] * (len(arr) - len(nz))
    return nz + zeros


def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    n, *rest = data
    arr = rest[:n]
    result = move_zero_to_end(arr)
    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
