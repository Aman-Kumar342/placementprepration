import heapq
from collections import defaultdict


def dijkstra(num_vertices, edges, source=0):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    dist = [float('inf')] * num_vertices
    dist[source] = 0
    pq = [(0, source)]
    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue
        for nei, w in graph[node]:
            nd = d + w
            if nd < dist[nei]:
                dist[nei] = nd
                heapq.heappush(pq, (nd, nei))
    return dist


if __name__ == "__main__":
    n = 5
    edges = [
        (0, 1, 2), (0, 3, 1), (1, 2, 3), (2, 4, 1), (3, 4, 6)
    ]
    print(dijkstra(n, edges, 0))
