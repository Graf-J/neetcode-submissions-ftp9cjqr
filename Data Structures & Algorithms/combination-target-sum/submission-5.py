class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(i, path, current):
            if current == target:
                result.append(path.copy())
                return
            if current > target or i >= len(nums):
                return
            
            path.append(nums[i])
            dfs(i, path, current + nums[i])
            path.pop()
            dfs(i + 1, path, current)

        dfs(0, [], 0)
        return result