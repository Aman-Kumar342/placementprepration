import sys


def majority_element(nums):
    n = len(nums)
    for i, val in enumerate(nums):
        if sum(1 for x in nums if x == val) > n // 2:
            return val
    return -1


def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    n, *rest = data
    arr = rest[:n]
    print(majority_element(arr))


if __name__ == "__main__":
    main()
