class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def dfs(i: int, j: int) -> int:
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]

            result = 0
            if s[i] == t[j]:
                result += dfs(i + 1, j + 1)
            result += dfs(i + 1, j)

            memo[(i, j)] = result
            return result

        return dfs(0, 0)





# s = xxyxy
# t = xy

                               
#                                 (0,0)           
#             (1,1)                                   (1,0)
#                         (2,1)
#                 (3,2)           (3,1)   
#                  {1}                    (4,1)
#                                 (5,2)           (5,1)
#                                  {1}             {0}
            
            