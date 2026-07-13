class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        last_max = last_min = 1

        result = float("-inf")
        for num in nums:
            tmp = num * last_max
            last_max = max(num, tmp, num * last_min)
            last_min = min(num, tmp, num * last_min)
            result = max(result, last_max)

        return result



