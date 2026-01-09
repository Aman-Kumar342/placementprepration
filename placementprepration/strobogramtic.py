import sys

PAIRS = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}


def is_strobogrammatic(num_str):
    left, right = 0, len(num_str) - 1
    while left <= right:
        l, r = num_str[left], num_str[right]
        if l not in PAIRS or PAIRS[l] != r:
            return False
        left += 1
        right -= 1
    return True


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n_str = data[0]
    if is_strobogrammatic(n_str):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
