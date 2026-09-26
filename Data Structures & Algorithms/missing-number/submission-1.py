class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = 0
        for i, num in enumerate(nums, start=1):
            missing ^= i
            missing ^= num

        return missing