class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        dp = [False] * len(nums)
        dp[target] = True
        for i in range(target - 1, -1, -1):
            for j in range(i + 1, min(i + nums[i] + 1, len(nums))):
                if dp[j]:
                    dp[i] = True
                    break

        return dp[0]




# dp[i] = any(dp[i + 1], ..., dp[i + nums[i]])

# [1,2,0,1,0]
# [F,F,F,F,T]

# [T,T,F,T,T]