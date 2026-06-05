class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        result = float("inf")
        while l <= r:
            m = (l + r) // 2
            result = min(result, nums[m])
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1

        return result





# [4,5,6,1,2,3] -> Go to left but keep m
# [4,5,6,1] -> Go to right
# [1]

# [4,5,6,1,2,3] -> Store 1
# [4,5,6] -> Min(5,1)
# [4] -> Min(4,1)

# [3,4,5,6,1,2] -> Sture 6
# [1,2] -> Min(2, 6)
# [1] -> Min(1, 2)

# [6,1,2,3,4,5] -> Store 3
# [6, 1, 2] -> Min(3, 1)
# [6] -> Min(6, 1)

# [1,2,3,4,5,6] -> Store 4
# [1, 2, 3] -> Min(4, 2)
# [1] -> Min(2, 1)