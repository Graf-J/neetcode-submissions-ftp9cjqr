class DSU:
    def __init__(self, n: int):
        self.parents = list(range(n))
        self.sizes = [1] * n

    def find(self, u: int) -> int:
        if self.parents[u] != u:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u: int, v: int) -> bool:
        ru, rv = self.find(u), self.find(v)
        if ru == rv:
            return False

        if self.sizes[ru] < self.sizes[rv]:
            ru, rv = rv, ru

        self.parents[rv] = ru
        self.sizes[ru] += self.sizes[rv]
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for a, b in edges:
            if dsu.union(a, b):
                n -= 1

        return n
