class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(i: int, current: int) -> int:
            if i == len(nums) and current == 0:
                return 1
            if i == len(nums):
                return 0
            if (i, current) in memo:
                return memo[(i, current)]

            memo[(i, current)] = dfs(i + 1, current - nums[i]) + dfs(i + 1, current + nums[i])
            return memo[(i, current)]

        return dfs(0, target)




#                         (0, 2)
#             (1,0)                   (1,4)
#     (2,-2)          (2,2)       (2,2)    (2,6)
# (3,0)  (3,-4)   (3,4)   (3,0) (3,4) (3,0)