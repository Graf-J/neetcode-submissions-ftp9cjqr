class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(2, n + 1):
            one, two = two, one + two
        return two


    # dp[i] = dp[i + 1] + dp[i + 2]

    # n = 3
    # [1, 1, ?, ?]
    # [1, 1, 2, ?]
    # [1, 1, 2, 3]

    # n = 3
    # [?, ?, 1, 1] (len = 4)
    # [?, 2, 1, 1]
    # [3, 2, 1, 1]


    #             (0)
    #             r:2
    #     (1)             (2)
    #     r:1             r:1
    # (1)     (3)         
    # r:1     r:0  



