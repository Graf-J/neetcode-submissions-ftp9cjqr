class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        result = 0
        for i in range(n):
            result ^= i
        for n in nums:
            result ^= n

        return result


# 0 ^ 1 ^ 2 ^ 3       ^ 3 ^ 0 ^ 1
# (0 ^ 0) ^ (1 ^ 1) ^ (3 ^ 3) ^ 2
#    0         0         0      2

# 0 ^ 0 = 0
# 0 ^ 2 = 2

# -> First iterate through all numbers, then through the list with the missing number