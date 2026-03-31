class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for idx, n in enumerate(nums):
            if hashmap.get(target - n) is not None:
                return [hashmap.get(target - n), idx]

            hashmap[n] = idx