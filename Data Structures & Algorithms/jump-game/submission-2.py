class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1

        memo = set()
        def dfs(i: int) -> bool:
            if i == target:
                return True
            if i > target or nums[i] == 0:
                return False
            if i in memo:
                return False

            if any(dfs(i_next) for i_next in range(i + 1, i + nums[i] + 1)):
                return True
            memo.add(i)
            return False

        return dfs(0)



