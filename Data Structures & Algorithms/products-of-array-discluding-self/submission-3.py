class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Prefix
        prefix, temp = [1], 1
        for num in nums:
            temp *= num
            prefix.append(temp)
        del prefix[-1]

        # Suffix
        suffix, temp = [1], 1
        for num in reversed(nums):
            temp *= num
            suffix.append(temp)
        del suffix[-1]

        # Product
        result = []
        for prefix, suffix in zip(prefix, reversed(suffix)):
            result.append(prefix * suffix)

        return result


# [2, 2, 3, 4, 5]

# Prefix:  [1,   2,  4,  12, 48]
# Postfix: [120, 60, 20, 5,  1 ]




