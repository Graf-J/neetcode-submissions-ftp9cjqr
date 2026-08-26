class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res_idx = {}
        for i, num in enumerate(nums):
            if num in res_idx:
                return [res_idx[num], i]
            
            res_idx[target - num] = i

        return [-1, -1]



# [3,4,5,6]

# res_idx = {
#     4: 0

# }