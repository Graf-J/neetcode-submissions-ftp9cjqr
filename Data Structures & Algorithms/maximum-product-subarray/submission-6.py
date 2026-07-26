class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_val = min_val = result = nums[0]
        for i in range(1, len(nums)):
            min_val, max_val = (
                min(min_val * nums[i], max_val * nums[i], nums[i]),
                max(min_val * nums[i], max_val * nums[i], nums[i])
            )
            result = max(result, max_val)

        return result


        


# [2, 4, -3, 5]
#     ^


# max_val = 8
# min_val = 2


