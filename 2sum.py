import sys


def two_sum_exists(nums, target):
    seen = set()
    for num in nums:
        if target - num in seen:
            return True
        seen.add(num)
    return False


def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    if len(data) < 2:
        print("The two not exist in the array ")
        return
    n, target, *rest = data
    nums = rest[:n]
    if two_sum_exists(nums, target):
        print("the two sum exit in the array ")
    else:
        print("The two not exist in the array ")


if __name__ == "__main__":
    main()
