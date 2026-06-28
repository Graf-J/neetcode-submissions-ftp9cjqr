class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, u: int) -> int:
        if u != self.parent[u]:
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
    def distance(self, a: List[int], b: List[int]) -> int:
        a_x, a_y = a
        b_x, b_y = b
        return abs(a_x - b_x) + abs(a_y - b_y)

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        point_distances = []
        for i, p1 in enumerate(points):
            for j in range(i + 1, len(points)):
                p2 = points[j]
                d = self.distance(p1, p2)
                point_distances.append((d, i, j))
        heapq.heapify(point_distances)

        dsu = DSU(len(points))
        result = 0
        ctr = 0
        while point_distances:
            d, p1, p2 = heapq.heappop(point_distances)
            if dsu.union(p1, p2):
                result += d
                ctr += 1

            if ctr == len(points) - 1:
                break

        return result








