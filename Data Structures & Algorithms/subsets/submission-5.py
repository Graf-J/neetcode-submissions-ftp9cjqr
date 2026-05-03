class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(i, subset):
            if i >= len(nums):
                result.append(subset[:])
                return

            dfs(i + 1, subset + [nums[i]])
            dfs(i + 1, subset)

        dfs(0, [])
        return result









