import sys

def count_unique(arr):
    return len(set(arr))


def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    n, *rest = data
    arr = rest[:n]
    print(count_unique(arr))


if __name__ == "__main__":
    main()
