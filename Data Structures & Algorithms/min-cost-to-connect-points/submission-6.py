class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, u: int) -> int:
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u: int, v: int) -> bool:
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False

        if self.size[pu] < self.size[pv]:
            pu, pv = pv, pu

        self.parent[pv] = pu
        self.size[pu] += self.size[pv]

        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                (x1, y1), (x2, y2) = points[i], points[j]
                d = abs(x2 - x1) + abs(y2 - y1)
                edges.append((d, i, j))
        heapq.heapify(edges)

        dsu = DSU(n)
        num_edges = 0
        result = 0
        while num_edges < n - 1:
            d, u, v = heapq.heappop(edges)
            if dsu.union(u, v):
                result += d
                num_edges += 1

        return result
        




