class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for idx in range(len(nums)):
            if target - nums[idx] in cache:
                return [cache[target - nums[idx]], idx]

            cache[nums[idx]] = idx

        return [-1, -1]
