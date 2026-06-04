class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        exists = set()
        for num in nums:
            if num in exists:
                return True
            exists.add(num)

        return False