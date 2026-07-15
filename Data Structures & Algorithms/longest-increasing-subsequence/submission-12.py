class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        def dfs(i: int) -> int:
            if memo[i] != -1:
                return memo[i]

            lis = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    lis = max(lis, 1 + dfs(j))

            memo[i] = lis
            return lis

        return max(dfs(i) for i in range(len(nums)))








#                             O
# 9              1                 4           
#            4 2 3 3 7
#         7








