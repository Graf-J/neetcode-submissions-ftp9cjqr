class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dfs(r: int, c: int) -> int:
            if r == m - 1 and c == n - 1:
                return 1
            if r == m or c == n:
                return 0
            if (r, c) in memo:
                return memo[(r, c)]

            memo[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
            return memo[(r, c)]

        return dfs(0, 0)








        #                 (0,0)
        #                 r:2
        #     (1,0)                   (0,1)
        #     r:1                     r:1
        # (2,0)   (1,1)           (1,1)   (0,2)
        # r:0     r:1             r:1     r:0