class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dfs(i: int, j: int) -> bool:
            if (i, j) in memo:
                return memo[(i, j)]

            # Pattern completely consumed
            if j == len(p):
                return i == len(s)

            # Does the current character match?
            first_match = (
                i < len(s) and
                (s[i] == p[j] or p[j] == ".")
            )

            # Is the next pattern character a '*'?
            if j + 1 < len(p) and p[j + 1] == "*":
                ans = (
                    dfs(i, j + 2) or                  # skip x*
                    (first_match and dfs(i + 1, j))  # use one x
                )
            else:
                ans = first_match and dfs(i + 1, j + 1)

            memo[(i, j)] = ans
            return ans

        return dfs(0, 0)
        





# s = "aa", p = ".b"
#                                 (0,0)
#                                 (1,1)
#                                   x


# s = "nnn", p = "n*"
#                                 (0,0)
#                                 (1,1)
#                     ()                     (1,0)


# s = "abc", p = "ax*b."