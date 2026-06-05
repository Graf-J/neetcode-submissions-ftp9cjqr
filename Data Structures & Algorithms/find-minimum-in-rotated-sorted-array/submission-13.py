class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)
        while l < r - 1:
            m = (l + r - 1) // 2
            if nums[m] > nums[r - 1]:
                l = m + 1
            else:
                r = m + 1

        return nums[l]

            
# [1,2,3,4,5,6]

# [3,4,5,6,1,2] l=0;r=6;m=3
# [1,2]         l=4;r=6;m=5


# [4,5,6,1,2,3] l=0;r=6;m=3
# [4,5,6,1] l=0;r=4;m=2
# [1] l=3;r=4

# [6,1,2,3,4,5]
