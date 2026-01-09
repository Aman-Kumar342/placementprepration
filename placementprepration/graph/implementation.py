import sys


def build_adj_matrix(n, edges):
    matrix = [[0] * (n + 1) for _ in range(n + 1)]
    for u, v in edges:
        matrix[u][v] = 1
        matrix[v][u] = 1
    return matrix


def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if len(data) < 2:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        edges.append((u, v))
    matrix = build_adj_matrix(n, edges)
    for row in matrix:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    main()
