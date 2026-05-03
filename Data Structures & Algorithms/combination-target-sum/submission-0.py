class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result, trace, total = [], [], 0
        def dfs(i):
            nonlocal total
            if total == target:
                result.append(trace[:])
                return
            elif total > target:
                return

            for idx in range(i, len(nums)):
                trace.append(nums[idx])
                total += nums[idx]
                dfs(idx)
                trace.pop()
                total -= nums[idx]

        dfs(0)
        return result