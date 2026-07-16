import heapq

# ---------- Union-Find for Kruskal ----------
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)

        if rx == ry:
            return False

        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx

        self.parent[ry] = rx

        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1

        return True


# ---------- Kruskal's Algorithm ----------
def kruskal(n, edges):
    edges = sorted(edges)

    uf = UnionFind(n)
    mst = []
    cost = 0

    for w, u, v in edges:
        if uf.union(u, v):
            mst.append((u, v, w))
            cost += w

    return mst, cost


# ---------- Prim's Algorithm ----------
def prim(n, adj, start=0):
    INF = float("inf")

    key = [INF] * n
    parent = [-1] * n
    visited = [False] * n

    key[start] = 0
    pq = [(0, start)]

    mst = []
    cost = 0

    while pq:
        w, u = heapq.heappop(pq)

        if visited[u]:
            continue

        visited[u] = True

        if parent[u] != -1:
            mst.append((parent[u], u, w))
            cost += w

        for v, wt in adj.get(u, []):
            if not visited[v] and wt < key[v]:
                key[v] = wt
                parent[v] = u
                heapq.heappush(pq, (wt, v))

    return mst, cost


# ---------- Graph Definition ----------
n = 12

edges = [
    (6, 0, 3),
    (4, 3, 9),
    (6, 3, 7),
    (3, 7, 8),
    (8, 6, 4),
    (4, 2, 6),
    (12, 9, 10),
    (15, 5, 11),

    # Extra edges (not selected in the MST)
    (10, 0, 7),
    (9, 3, 6),
    (14, 8, 9),
    (20, 4, 5),
    (18, 1, 2)
]

# ---------- Build Adjacency List ----------
adj = {}

for w, u, v in edges:
    adj.setdefault(u, []).append((v, w))
    adj.setdefault(v, []).append((u, w))

# ---------- Run Algorithms ----------
k_mst, k_cost = kruskal(n, edges)
p_mst, p_cost = prim(n, adj, start=0)

# ---------- Display Results ----------
print("=== Kruskal's MST ===")
for u, v, w in k_mst:
    print(f"Edge ({u} - {v}) Weight: {w}")
print(f"Total Kruskal Cost: {k_cost}")

print("\n=== Prim's MST (starting from Node 0) ===")
for u, v, w in p_mst:
    print(f"Edge ({u} - {v}) Weight: {w}")
print(f"Total Prim Cost: {p_cost}")
