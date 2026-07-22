class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def dfs(i: int, j: int) -> bool:
            if i == len(s) and j == len(p):
                return True
            if j == len(p):
                return False
            if (i, j) in memo:
                return memo[(i, j)]

            chars_match = (
                i < len(s) and
                (s[i] == p[j] or p[j] == ".")
            )
            if j < len(p) - 1 and p[j + 1] == "*":
                memo[(i, j)] = (
                    dfs(i, j + 2) or # skip
                    chars_match and dfs(i + 1, j) # take
                )
                return memo[(i, j)]
            
            if chars_match:
                memo[(i, j)] = dfs(i + 1, j + 1)
                return memo[(i, j)]

            memo[(i, j)] = False
            return memo[(i, j)]

        return dfs(0, 0)











# s = "nnn", p = "n*"

#                                 (0,0)
#             (0, 2)                                  (1, 0)
#                x                       (1,2)                    (2,0)
#                                          x              (2,2)           (3,0) -> n* still remains even though i == len(s) -> continue
#                                                           x         (3,2)   (4,0)
#                                                                       v       -> not executed anymore (short circuit)                