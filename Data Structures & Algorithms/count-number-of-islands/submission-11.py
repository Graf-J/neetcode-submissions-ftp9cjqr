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

        return True

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        dsu = DSU(ROW * COL)

        def index(r: int, c: int) -> int:
            return r * COL + c

        num_islands = 0
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == "1":
                    num_islands += 1
                    for nr, nc in ((row - 1, col), (row + 1, col), (row, col + 1), (row, col - 1)):
                        if (
                            0 <= nr < ROW and
                            0 <= nc < COL and
                            grid[nr][nc] == "1" and
                            dsu.union(index(row, col), index(nr, nc))
                        ):
                            num_islands -= 1

        return num_islands
        
        