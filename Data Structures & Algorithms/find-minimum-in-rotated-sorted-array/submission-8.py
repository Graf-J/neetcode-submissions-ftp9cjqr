import os

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if right_clean := nums[m] < nums[r]:
                r = m
            else:
                l = m + 1

        return nums[m]


# Scenario (0)
# [1, 2, [3], 4, 5]
# [[1], 2]
# [1]

# Scenario (1)
# [5, 6, [1], 2, 3, 4]
# [5, [6], 1]
# [[6], 1]


# Scenario (2)
# [3, 4, [5], 6, 1, 2]
# [5, [6], 1, 2]
# [6, [1], 2]
# 

# Scenario (3)
# [6, 1, [2], 3, 4, 5]
# [6, [1], 2]
# [[6], 1]
# [1]

# Scenario (4)
# [3, 4, [5], 1, 2]
# 



