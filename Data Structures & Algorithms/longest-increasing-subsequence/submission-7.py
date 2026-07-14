class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

# nums=[9,1,4,2,3,3,7]
# dp  =[1,4,2,3,2,2,1]


# nums = [1, 5, -2, 3, 4]

# dp = [3, 1, 3, 2, 1]




    #             O
    #     2       1       7
    # (1)    7    7       x
    #        x    x