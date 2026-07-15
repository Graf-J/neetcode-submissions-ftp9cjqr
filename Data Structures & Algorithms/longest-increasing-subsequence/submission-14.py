class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                dp[i] = max(dp[i], 1 + dp[j]) if nums[j] > nums[i] else dp[i]

        return max(dp)




# nums = [9,1,4,2,3,3,7]

# dp =   [-1, -1, -1, -1, -1, -1, 1]

# dp[i] = max(1 + dp[i + 1:] if nums[i] < nums[j])







