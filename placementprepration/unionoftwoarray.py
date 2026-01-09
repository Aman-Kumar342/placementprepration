import sys


def union_arrays(a, b):
    return sorted(set(a) | set(b))


def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if len(data) < 2:
        return
    n, m, *rest = data
    a = rest[:n]
    b = rest[n : n + m]
    res = union_arrays(a, b)
    print(" ".join(map(str, res)))


if __name__ == "__main__":
    main()
