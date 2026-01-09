import sys


def max_product_subarray(nums):
    n = len(nums)
    best = -2147483648
    for i in range(n):
        prod = 1
        for j in range(i, n):
            prod *= nums[j]
            best = max(best, prod)
    return best


def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    n, *rest = data
    arr = rest[:n]
    print(max_product_subarray(arr))


if __name__ == "__main__":
    main()
