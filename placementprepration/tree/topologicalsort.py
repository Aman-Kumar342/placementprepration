from collections import defaultdict


def topo_sort(num_vertices, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    visited = [False] * num_vertices
    stack = []

    def dfs(node):
        visited[node] = True
        for nei in graph[node]:
            if not visited[nei]:
                dfs(nei)
        stack.append(node)

    for v in range(num_vertices):
        if not visited[v]:
            dfs(v)
    return stack[::-1]


if __name__ == "__main__":
    n = 6
    edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
    print(topo_sort(n, edges))
