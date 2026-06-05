class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[l] < nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r - 1]:
                    l = m + 1
                else:
                    r = m

        return -1




# [3,4,5,6,1,2]
# target = 1

# l = 4
# r = 5

# m = 4
# nums[m] = 1