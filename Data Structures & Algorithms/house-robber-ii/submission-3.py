class Solution:
    def rob_1D(self, nums: List[int], first: int, last: int):
        memo = {}
        def dfs(i: int) -> int:
            if i >= last + 1:
                return 0
            if i in memo:
                return memo[i]

            memo[i] = nums[i] + max(dfs(i + 2), dfs(i + 3))
            return memo[i]

        return max(dfs(first), dfs(first + 1))


    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(
            self.rob_1D(nums, 0, len(nums) - 2),
            self.rob_1D(nums, 1, len(nums) - 1)
        )