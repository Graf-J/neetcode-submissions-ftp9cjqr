class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_val = max_val = result = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            min_val, max_val = (
                min(nums[i], nums[i] * max_val, nums[i] * min_val),
                max(nums[i], nums[i] * max_val, nums[i] * min_val),
            )
            result = max(result, max_val)

        return result