import sys


def find_missing(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(nums)


def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    m, *rest = data
    arr = rest[:m]
    print(find_missing(arr))


if __name__ == "__main__":
    main()
