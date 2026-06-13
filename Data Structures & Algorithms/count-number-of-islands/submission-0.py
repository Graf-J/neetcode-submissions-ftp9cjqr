class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        def bfs(row, col) -> bool:
            island_found = False
            q = deque([(row, col)])
            while q:
                r, c = q.popleft()
                if grid[r][c] == "0":
                    continue
                else:
                    grid[r][c] = "0"
                    island_found = True    
            
                directions = ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1))
                for r_new, c_new in directions:
                    if not (
                        r_new < 0 or r_new == len(grid) or
                        c_new < 0 or c_new == len(grid[0])
                    ):
                        q.append((r_new, c_new))

            return island_found

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                result += bfs(row, col)

        return result

            










