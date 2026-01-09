import sys


def longest_subarray_with_sum_k(arr, k):
    i = 0
    curr = 0
    best = 0
    for j, val in enumerate(arr):
        curr += val
        while curr > k and i <= j:
            curr -= arr[i]
            i += 1
        if curr == k:
            best = max(best, j - i + 1)
    return best


def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if len(data) < 2:
        return
    n, k, *rest = data
    arr = rest[:n]
    print(longest_subarray_with_sum_k(arr, k))


if __name__ == "__main__":
    main()
