class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i: int):
            if i in memo:
                return memo[i]

            result = 0
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    result = max(result, dfs(j))

            memo[i] = result + 1
            return result + 1

        return max(dfs(i) for i in range(len(nums)))














            #                 (1)
            # (2)     (3)     (4)     (5)     (6)
            # (6)  (4)(5)(6)