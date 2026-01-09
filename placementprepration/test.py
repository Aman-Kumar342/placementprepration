import sys


def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    a, *rest = data
    b = rest[:a]
    if not b:
        return
    print(min(b))


if __name__ == "__main__":
    main()
