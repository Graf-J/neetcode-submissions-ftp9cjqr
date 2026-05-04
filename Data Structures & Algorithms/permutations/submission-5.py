class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(path, used):
            if len(path) == len(nums):
                result.append(path.copy())

            for i in range(len(nums)):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i] = True
                dfs(path, used)
                path.pop()
                used[i] = False

        dfs([], [False] * len(nums))
        return result