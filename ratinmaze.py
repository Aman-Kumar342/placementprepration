import sys
from typing import List


class Choice:
    def __init__(self, dx: int, dy: int, name: str):
        self.dx = dx
        self.dy = dy
        self.name = name


def is_solved(x: int, y: int, n: int) -> bool:
    return x == n - 1 and y == n - 1


def is_valid(x: int, y: int, n: int, grid: List[List[int]]) -> bool:
    return 0 <= x < n and 0 <= y < n and grid[x][y] == 1


def dfs(x: int, y: int, n: int, path: List[str], grid: List[List[int]], choices: List[Choice], res: List[str]):
    if is_solved(x, y, n):
        res.append("".join(path))
        return
    for choice in choices:
        nx, ny = x + choice.dx, y + choice.dy
        if is_valid(nx, ny, n, grid):
            grid[x][y] = 0
            path.append(choice.name)
            dfs(nx, ny, n, path, grid, choices, res)
            path.pop()
            grid[x][y] = 1


def find_paths(grid: List[List[int]]) -> List[str]:
    n = len(grid)
    if n == 0 or grid[0][0] == 0:
        return []
    choices = [Choice(-1, 0, "u"), Choice(1, 0, "d"), Choice(0, -1, "l"), Choice(0, 1, "r")]
    res = []
    dfs(0, 0, n, [], grid, choices, res)
    return res


def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    n, *rest = data
    vals = rest[: n * n]
    grid = [vals[i * n : (i + 1) * n] for i in range(n)]
    paths = find_paths(grid)
    if not paths:
        print("No path found")
    else:
        for p in paths:
            print(p)


if __name__ == "__main__":
    main()
