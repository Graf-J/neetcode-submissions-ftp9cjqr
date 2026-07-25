class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dfs(i: int) -> int:
            if i == len(s):
                return 1
            if i > len(s):
                return 0
            if s[i] == "0":
                return 0
            if i in memo:
                return memo[i]

            result = dfs(i + 1)
            if i < (len(s) - 1) and int(s[i:i+2]) <= 26:
                result += dfs(i + 2)

            memo[i] = result
            return result

        return dfs(0)



# s = "2712"

#                             (0)
#                             r:2
#                 (1)
#                 r:2
#         (2) 
#         r:2  
#     (3)     (4) 
#     r:1     r:1
#   (4)
#   r:1                 


# s = "1012"

#                     (0)
#                      2
#         (1)                     (2)
#         r:0                     r:2
#                            (3)       (4)
#                            r:1       r:1
#                         (4)   (5)
#                         r:1   r:0