class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        def dfs(i: int) -> int:
            if memo[i] != -1:
                return memo[i]

            max_depth = 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    max_depth = max(max_depth, 1 + dfs(j))

            memo[i] = max_depth
            return max_depth

        return max(dfs(i) for i in range(len(nums)))







    #             O
    #     2       1       7
    # (1)    7    7       x
    #        x    x