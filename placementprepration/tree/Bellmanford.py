import sys
from math import inf

class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight


def bellman_ford(edges, v, source):
    dist = [inf] * v
    dist[source] = 0
    for _ in range(v - 1):
        updated = False
        for eg in edges:
            if dist[eg.src] != inf and dist[eg.src] + eg.weight < dist[eg.dest]:
                dist[eg.dest] = dist[eg.src] + eg.weight
                updated = True
        if not updated:
            break
    return dist


def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if len(data) < 3:
        return
    it = iter(data)
    v = int(next(it))
    e = int(next(it))
    edges = []
    for _ in range(e):
        src = int(next(it))
        dest = int(next(it))
        wt = int(next(it))
        edges.append(Edge(src, dest, wt))
    source = int(next(it, 0))
    dist = bellman_ford(edges, v, source)
    print(" ".join("INF" if d == inf else str(d) for d in dist))


if __name__ == "__main__":
    main()
