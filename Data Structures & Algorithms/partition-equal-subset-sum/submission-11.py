class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n, s = len(nums), sum(nums)
        if s % 2:
            return False
        target = s // 2

        dp = [False] * (target + 1)
        dp[0] = True
        for r in range(1, target + 1):
            dp[r] = nums[-1] == r

        for i in range(len(nums) - 2, -1, -1):
            dp_tmp = [False] * (target + 1)
            for r in range(1, target + 1):
                take = nums[i] <= r and dp[r - nums[i]]
                dp_tmp[r] = dp[r] or take
            dp = dp_tmp

        return dp[target]

        # n = len(nums)
        # dp = [[False] * n for _ in range(target + 1)]
        # for r in range(1, target + 1):
        #     dp[r][-1] = nums[-1] == r

        # for i in range(len(nums) - 2, -1, -1):
        #     for r in range(1, target + 1):
        #         take = nums[i] <= r and dp[r - nums[i]][i + 1]
        #         dp[r][i] = dp[r][i + 1] or take

        # return dp[target][0]





# nums = [1,2,3,4]

# dp[remaining][i] = dp[remaining][i + 1] or dp[remaining - nums[i]][i + 1]
# Can handle remaining with numbers at i or later = (
#     Can handle remaining with numbers at i + 1 or later (if can handle later I can also handle here) or
#     If I add the current number at i than at i + 1 I have to be able to handle remaining - 1 to solve problem
# )

#     0  1  2  3    (i)
# 0   F  F  F  F    (dummy to make indexing easy)
# 1   ?  ?  ?  F
# 2   ?  ?  ?  F
# 3   ?  ?  ?  F
# 4   T  T  T  T
# 5   ?  ?  ?  F

# (r remaining)