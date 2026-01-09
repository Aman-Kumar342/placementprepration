from collections import defaultdict


def dfs_traversal(num_vertices, edges, start=0):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    visited = [False] * num_vertices
    order = []

    def dfs(node):
        visited[node] = True
        order.append(node)
        for nei in graph[node]:
            if not visited[nei]:
                dfs(nei)

    dfs(start)
    return order


if __name__ == "__main__":
    n = 5
    edges = [(0, 1), (0, 2), (1, 3), (1, 4)]
    print(dfs_traversal(n, edges, 0))
