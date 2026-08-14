class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = {}
        def dfs(i: int, to_close: int) -> bool:
            if i == len(s) and to_close == 0:
                return True
            if i == len(s) or to_close < 0:
                return False
            if (i, to_close) in memo:
                return memo[(i, to_close)]

            if s[i] == "(":
                memo[(i, to_close)] = dfs(i + 1, to_close + 1)
            elif s[i] == ")":
                memo[(i, to_close)] = dfs(i + 1, to_close - 1)
            else:
                memo[(i, to_close)] = (
                    dfs(i + 1, to_close - 1) or
                    dfs(i + 1, to_close) or
                    dfs(i + 1, to_close + 1)
                )

            return memo[(i, to_close)]

        return dfs(0, 0)




#                             (0,0)
#                             (1,1)
#                             (2,2)
#       (3,3)                 (3,2)                 (3,1)
# (4,4) (4,3) (4,2)     (4,3) (4,2) (4,1)    (4,2)  (4,1)  (4,0)
# (5,3) (5,2) (5,1)     (5,2) (5,1) (5,0)    (5,1)  (5,0)  (5,-1)