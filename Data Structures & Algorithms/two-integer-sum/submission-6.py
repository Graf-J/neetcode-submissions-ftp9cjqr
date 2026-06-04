class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_idx = {}
        for idx, num in enumerate(nums):
            if target - num in num_idx:
                return [
                    num_idx[target - num],
                    idx
                ]

            num_idx[num] = idx