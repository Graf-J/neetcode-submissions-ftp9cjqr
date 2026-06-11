class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(path, i):
            if i == len(nums):
                result.append(path.copy())
                return

            dfs(path, i + 1)
            path.append(nums[i])
            dfs(path, i + 1)
            path.pop()

        dfs([], 0)
        return result