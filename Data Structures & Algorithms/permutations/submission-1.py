class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(path, used):
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                dfs(path + [nums[i]], used)
                used[i] = False

        dfs([], [False] * len(nums))
        return result