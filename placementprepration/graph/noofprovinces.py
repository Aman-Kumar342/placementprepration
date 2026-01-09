import sys


def dfs(node, adj, vis):
    vis[node] = 1
    for nei in adj[node]:
        if not vis[nei]:
            dfs(nei, adj, vis)


def no_of_provinces(adj_matrix):
    v = len(adj_matrix)
    adj = [[] for _ in range(v)]
    for i in range(v):
        for j in range(v):
            if adj_matrix[i][j] == 1 and i != j:
                adj[i].append(j)
    vis = [0] * v
    ct = 0
    for i in range(v):
        if not vis[i]:
            ct += 1
            dfs(i, adj, vis)
    return ct


def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    it = iter(data)
    v = int(next(it))
    vals = [int(next(it)) for _ in range(v * v)]
    adj_matrix = [vals[i * v : (i + 1) * v] for i in range(v)]
    print(no_of_provinces(adj_matrix))


if __name__ == "__main__":
    main()
