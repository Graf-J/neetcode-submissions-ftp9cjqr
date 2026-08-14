class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        dp_prev = [False] * ((n // 2) + 1)
        dp_prev[0] = True
        
        for i in range(n - 1, -1, -1):
            dp_cur = [False] * ((n // 2) + 1)
            for to_close in range(n // 2, -1, -1):
                if s[i] == "(":
                    if to_close == (n // 2):
                        dp_cur[to_close] = False
                    else:
                        dp_cur[to_close] = dp_prev[to_close + 1]
                elif s[i] == ")":
                    # Edge case -1 works since it goes back to last dummy element (always F)
                    dp_cur[to_close] = dp_prev[to_close - 1] 
                else:
                    if to_close == (n // 2):
                        dp_cur[to_close] = (
                            dp_prev[to_close] or
                            dp_prev[to_close - 1]
                        )
                    else:
                        dp_cur[to_close] = (
                            dp_prev[to_close + 1] or
                            dp_prev[to_close] or
                            dp_prev[to_close - 1]
                        )
                
            dp_prev = dp_cur

        return dp_cur[0]


# dp[i][to_close] = (
#     if s[i] == "(": dp[i + 1][to_close + 1]
#     if s[i] == ")": dp[i + 1][to_close - 1]
#     if s[i] == "*": dp[...] or dp[...] or dp[...]
# )

#     c:0 c:1 c:2 c:d         (len(s) // 2)
# i:0              F
# i:1              F
# i:2              F
# i:3              F
# i:4  F   T   F   F
# i:d  T   F   F   F


#                             (0,0)
#                             (1,1)
#                             (2,2)
#       (3,3)                 (3,2)                 (3,1)
# (4,4) (4,3) (4,2)     (4,3) (4,2) (4,1)    (4,2)  (4,1)  (4,0)
# (5,3) (5,2) (5,1)     (5,2) (5,1) (5,0)    (5,1)  (5,0)  (5,-1)