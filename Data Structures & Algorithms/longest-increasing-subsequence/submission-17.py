class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            # dp[i] = 1 + max(dp[j] for j in range(i + 1, len(nums)) if nums[j] > nums[i])
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)




# dfs[i] = 1 + max(dfs[j] for j in range(i + 1, len(s)) if nums[j] > nums[i])

# dp = [?, ?, ?, ?, ?, ?, 1]











            #                 (1)
            # (2)     (3)     (4)     (5)     (6)
            # (6)  (4)(5)(6)