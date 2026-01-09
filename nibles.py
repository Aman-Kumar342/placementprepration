import sys


def swap_nibbles(n):
    right = (n & 0x0F) << 4
    left = (n >> 4) & 0x0F
    return right | left


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    print(swap_nibbles(n))


if __name__ == "__main__":
    main()
