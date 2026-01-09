import sys
from collections import deque


def bfs_traversal(adj):
    v = len(adj)
    vis = [0] * v
    q = deque([0])
    vis[0] = 1
    res = []
    while q:
        node = q.popleft()
        res.append(node)
        for nei in adj[node]:
            if not vis[nei]:
                vis[nei] = 1
                q.append(nei)
    return res


def dfs_helper(node, adj, vis, res):
    vis[node] = 1
    res.append(node)
    for nei in adj[node]:
        if not vis[nei]:
            dfs_helper(nei, adj, vis, res)


def dfs_traversal(adj):
    v = len(adj)
    vis = [0] * v
    res = []
    dfs_helper(0, adj, vis, res)
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
    print("BFS", " ".join(map(str, bfs_traversal(adj))))
    print("DFS", " ".join(map(str, dfs_traversal(adj))))


if __name__ == "__main__":
    main()
