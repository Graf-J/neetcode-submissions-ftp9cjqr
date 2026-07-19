class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(i: int, s: int) -> int:
            if i == len(nums) and s == target:
                return 1
            if i == len(nums) and s != target:
                return 0
            if (i, s) in memo:
                return memo[(i, s)]

            memo[(i, s)] = dfs(i + 1, s + nums[i]) + dfs(i + 1, s - nums[i])
            return memo[(i, s)]

        return dfs(0, 0)

    


# nums = [2, 2, 2]
# target = 2

#                         O
#                 2               -2
#             4       0       0       -4
#         6       22      -22     -2-2    -6