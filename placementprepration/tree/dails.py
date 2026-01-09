from collections import deque

class Edge:
    def __init__(self, to, weight):
        self.to = to
        self.weight = weight


def dials_algo(N, src, adj, w):
    inf = 10 ** 18
    dist = [inf] * N
    dist[src] = 0
    buckets = [deque() for _ in range(w * N + 1)]
    buckets[0].append(src)
    for d in range(w * N + 1):
        while buckets[d]:
            u = buckets[d].popleft()
            if dist[u] < d:
                continue
            for e in adj[u]:
                v, wt = e.to, e.weight
                if dist[v] > dist[u] + wt:
                    dist[v] = dist[u] + wt
                    buckets[dist[v]].append(v)
    return dist


def main():
    N = 5
    adj = [[] for _ in range(N)]
    adj[0].append(Edge(1, 2))
    adj[1].append(Edge(2, 1))
    adj[1].append(Edge(3, 3))
    adj[2].append(Edge(4, 4))
    adj[3].append(Edge(4, 2))
    maxweight = 4
    dist = dials_algo(N, 0, adj, maxweight)
    print("distance", dist)


if __name__ == "__main__":
    main()
