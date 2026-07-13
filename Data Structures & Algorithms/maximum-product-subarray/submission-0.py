class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp_max = [None] * len(nums)
        dp_min = [None] * len(nums)
        dp_max[0] = dp_min[0] = nums[0]

        result = dp_max[0]
        for i in range(1, len(nums)):
            tmp = dp_max[i - 1] * nums[i]
            dp_max[i] = max(nums[i], tmp, dp_min[i - 1] * nums[i])
            dp_min[i] = min(nums[i], tmp, dp_min[i - 1] * nums[i])
            
            result = max(result, dp_max[i])

        return result


        












# nums = [2, 4, -3, 5]
# dp   = [2, 8, -3, 5]


