import sys
from collections import deque


def distance(grid):
    n = len(grid)
    m = len(grid[0]) if n else 0
    vis = [[0] * m for _ in range(n)]
    dist = [[0] * m for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                q.append((i, j, 0))
                vis[i][j] = 1
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while q:
        r, c, step = q.popleft()
        dist[r][c] = step
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and vis[nr][nc] == 0:
                vis[nr][nc] = 1
                q.append((nr, nc, step + 1))
    return dist


def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if len(data) < 2:
        return
    n, m, *rest = data
    vals = rest[: n * m]
    grid = [vals[i * m : (i + 1) * m] for i in range(n)]
    res = distance(grid)
    for row in res:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    main()
