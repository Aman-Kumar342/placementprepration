import sys
from collections import deque


def bfs(adj):
    v = len(adj)
    vis = [0] * v
    vis[0] = 1
    q = deque([0])
    res = []
    while q:
        node = q.popleft()
        res.append(node)
        for nei in adj[node]:
            if not vis[nei]:
                vis[nei] = 1
                q.append(nei)
    return res


def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if len(data) < 2:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    res = bfs(adj)
    print(" ".join(map(str, res)))


if __name__ == "__main__":
    main()
