class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, v: int) -> int:
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

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
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        dsu = DSU(n)
        for a, b in edges:
            if not dsu.union(a, b):
                return False

        return True



