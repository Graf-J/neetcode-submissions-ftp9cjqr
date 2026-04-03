class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if left_clean := nums[l] <= nums[m]:
                if val_in_left := (nums[l] <= target <= nums[m]):
                    r = m
                else:
                    l = m + 1
            else:
                if val_in_right := (nums[m + 1] <= target <= nums[r]):
                    l = m + 1
                else:
                    r = m

        return l if nums[l] == target else -1


# [1, 2, [3], 4, 5, 6]
# [1, [2], 3]
# [3]


# [5, 6, [1], 2, 3, 4]
# [2, [3], 4]
# [[2], 3]


# [3, 4, [5], 6, 1, 2]


# [6, 1, [2], 3, 4, 5]


