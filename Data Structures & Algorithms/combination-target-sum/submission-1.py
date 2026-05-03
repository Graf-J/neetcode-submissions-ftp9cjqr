class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(i, trace, total):
            if total == target:
                result.append(trace[:])
                return
            if total > target or i >= len(nums):
                return

            trace.append(nums[i])
            dfs(i, trace, total + nums[i])
            trace.pop()
            dfs(i + 1, trace, total)

        dfs(0, [], 0)
        return result