import sys
from collections import deque


def oranges_rotting(grid):
    n = len(grid)
    m = len(grid[0]) if n else 0
    q = deque()
    vis = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                q.append((i, j, 0))
                vis[i][j] = 2
    time = 0
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while q:
        r, c, t = q.popleft()
        time = max(time, t)
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and vis[nr][nc] != 2 and grid[nr][nc] == 1:
                q.append((nr, nc, t + 1))
                vis[nr][nc] = 2
    for i in range(n):
        for j in range(m):
            if vis[i][j] != 2 and grid[i][j] == 1:
                return -1
    return time


def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if len(data) < 2:
        return
    n, m, *rest = data
    vals = rest[: n * m]
    grid = [vals[i * m : (i + 1) * m] for i in range(n)]
    print(oranges_rotting(grid))


if __name__ == "__main__":
    main()
