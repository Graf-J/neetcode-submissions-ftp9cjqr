class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_max_sum = nums[0]
        for i in range(1, len(nums)):
            current_max_sum = max(current_max_sum + nums[i], nums[i])
            max_sum = max(max_sum, current_max_sum)
        return max_sum