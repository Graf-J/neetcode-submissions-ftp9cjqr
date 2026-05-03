class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(path, used, depth):
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                dfs(path + [nums[i]], used, depth + 1)
                used[i] = False

            if depth == len(nums):
                result.append(path[:])

        dfs([], [False] * len(nums), 0)
        return result