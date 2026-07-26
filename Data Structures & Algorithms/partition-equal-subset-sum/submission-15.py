class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2

        dp_prev = [False] * (target + 1)
        dp_prev[0] = True

        for i in range(len(nums) - 1, -1, -1):
            dp_cur = [False] * (target + 1)
            dp_cur[0] = True
            for remaining in range(1, target + 1):
                dp_cur[remaining] |= dp_prev[remaining]
                if remaining - nums[i] >= 0:
                    dp_cur[remaining] |= dp_prev[remaining - nums[i]]
            dp_prev = dp_cur

        return dp_prev[target]



# dp[i][remaining] = dp[i + 1][remaining] or dp[i + 1][remaining - nums[i]]

# nums = [1, 2, 3, 4]
# target = 5

# dp = [T, ?, ?, ?, ?, ?]
#      [T, ?, ?, ?, ?, ?]
#      [T, ?, ?, ?, ?, ?]
#      [T, ?, ?, ?, ?, ?]
#      [T, F, F, F, F, F]