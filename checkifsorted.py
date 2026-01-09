import sys


def is_sorted(arr):
    # Verifies non-decreasing order across the whole array
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    n, *rest = data
    arr = rest[:n]
    if is_sorted(arr):
        print("the array is sorted")
    else:
        print("the array is not sorted")


if __name__ == "__main__":
    main()
