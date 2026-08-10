# DP: Top-Down
class Solution:
    def jump(self, nums: List[int]) -> int:
        target = len(nums) - 1

        memo = {}
        def dfs(i: int):
            if i == target:
                return 0
            if i > target or nums[i] == 0:
                return float("inf")
            if i in memo:
                return memo[i]

            memo[i] = 1 + min(dfs(i_next) for i_next in range(i + 1, i + nums[i] + 1))
            return memo[i]

        return dfs(0)











#                             (0)
#             (1)                             (2)
# (2)     (3)     (4)     (5)                 (3)
#                                             (4)
#                                             (5)