class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROW, COL = len(matrix), len(matrix[0])
        adj = defaultdict(list)
        indegree = defaultdict(int)
        for r in range(ROW):
            for c in range(COL):
                for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if (
                        0 <= nr < ROW and
                        0 <= nc < COL and
                        matrix[nr][nc] > matrix[r][c]
                    ):
                        adj[(r, c)].append((nr, nc))
                        indegree[(nr, nc)] += 1

        q = deque((r, c, 1) for r in range(ROW) for c in range(COL) if indegree[(r, c)] == 0)

        max_path_len = 0
        while q:
            r, c, path_len = q.popleft()
            max_path_len = max(max_path_len, path_len)
            for nr, nc in adj[(r, c)]:
                indegree[(nr, nc)] -= 1
                if indegree[(nr, nc)] == 0:
                    q.append((nr, nc, path_len + 1))

        return max_path_len





#      5    5 <- 3
#      ^    ^    |
#      |    |    v
# 1 -> 2 -> 3 -> 6
#           ^    ^
#           |    |
#           1    1