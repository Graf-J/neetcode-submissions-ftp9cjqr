class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        nums[-2] = max(nums[-2:])
        for i in range(len(nums) - 3, -1, -1):
            nums[i] = max(nums[i] + nums[i + 2], nums[i + 1])

        return nums[0]





'''
# Formula
[2, 9, 8, 3, 6]
max(nums[0] + rob[2:], rob[1:])

# Step 0
[?, ?, ?, 6, 6] max(3, 6), max(3, 6) Initialization
       ^
? = max(8 + 6, 6) = 14

# Step 1
[?, ?, 14, 6, 6]
    ^
? = max(9 + 6, 14) = 15

# Step 2
[?, 15, 14, 6, 6]
 ^
? = max(2 + 14, 15) = 16

# Result
[(16), 15, 14, 6, 6]
'''



