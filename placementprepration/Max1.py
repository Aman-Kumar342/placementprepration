import sys


def max_consecutive_ones(n):
    binary = bin(n)[2:]
    max_count = 0
    count = 0
    for digit in binary:
        if digit == "1":
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    print(max_consecutive_ones(n))


if __name__ == "__main__":
    main()
