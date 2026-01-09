import sys


def max_hourglass_sum(mat):
    n = len(mat)
    m = len(mat[0]) if n else 0
    if n < 3 or m < 3:
        return -1
    best = -2147483648
    for i in range(n - 2):
        for j in range(m - 2):
            s = (
                mat[i][j]
                + mat[i][j + 1]
                + mat[i][j + 2]
                + mat[i + 1][j + 1]
                + mat[i + 2][j]
                + mat[i + 2][j + 1]
                + mat[i + 2][j + 2]
            )
            best = max(best, s)
    return best


def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if len(data) < 2:
        return
    n, m, *rest = data
    vals = rest[: n * m]
    mat = [vals[i * m : (i + 1) * m] for i in range(n)]
    print(max_hourglass_sum(mat))


if __name__ == "__main__":
    main()
