class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dfs(prev_idx: int, current_idx: int) -> int:
            if current_idx == len(nums):
                return 0
            if (prev_idx, current_idx) in memo:
                return memo[(prev_idx, current_idx)]

            max_depth = dfs(prev_idx, current_idx + 1)
            if prev_idx == -1 or nums[current_idx] > nums[prev_idx]:
                max_depth = max(max_depth, 1 + dfs(current_idx, current_idx + 1))

            memo[(prev_idx, current_idx)] = max_depth
            return max_depth

        return dfs(-1, 0)