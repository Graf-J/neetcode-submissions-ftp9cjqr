class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        def dfs(i: int, path: List[int]) -> None:
            if i == len(nums):
                result.append(path.copy())
                return

            # Left Branch
            path.append(nums[i])
            dfs(i + 1, path)
            path.pop()

            # Right Branch
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, path)

        dfs(0, [])
        return result