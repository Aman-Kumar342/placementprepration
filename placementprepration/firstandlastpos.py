import sys


def find_first(nums, target):
    lo, hi = 0, len(nums) - 1
    pos = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            pos = mid
            hi = mid - 1
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return pos


def find_last(nums, target):
    lo, hi = 0, len(nums) - 1
    pos = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            pos = mid
            lo = mid + 1
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return pos


def search_range(nums, target):
    return [find_first(nums, target), find_last(nums, target)]


def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if len(data) < 2:
        return
    n, target, *rest = data
    nums = rest[:n]
    res = search_range(nums, target)
    print(" ".join(map(str, res)))


if __name__ == "__main__":
    main()
