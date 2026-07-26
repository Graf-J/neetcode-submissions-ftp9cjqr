class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2

        dp = [[False] * (target + 1) for _ in range(len(nums) + 1)]
        for i in range(len(nums) + 1):
            dp[i][0] = True

        for i in range(len(nums) - 1, -1, -1):
            for remaining in range(1, target + 1):
                dp[i][remaining] |= dp[i + 1][remaining]
                if remaining - nums[i] >= 0:
                    dp[i][remaining] |= dp[i + 1][remaining - nums[i]]

        return dp[0][target]



# dp[i][remaining] = dp[i + 1][remaining] or dp[i + 1][remaining - nums[i]]

# nums = [1, 2, 3, 4]
# target = 5

# dp = [T, ?, ?, ?, ?, ?]
#      [T, ?, ?, ?, ?, ?]
#      [T, ?, ?, ?, ?, ?]
#      [T, ?, ?, ?, ?, ?]
#      [T, F, F, F, F, F]