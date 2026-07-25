class Solution:
    def rob(self, nums: List[int]) -> int:
        left = mid = right = 0
        for i in range(len(nums) - 1, -1, -1):
            left, mid, right = (
                nums[i] + max(mid, right),
                left,
                mid
            )
        return max(left, mid)


# dp[i] = nums[i] + max(dp[i + 2], dp[i + 3])

# nums = [1, 1, 3, 3]

# dp = [?, ?, ?, ?, 0, 0, 0]

    #             (0)
    #             r:4
    #     (2)             (3)
    #     r:3             r:3
    # (4)     (5)     (5)     (6)
    # r:0     r:0     r:0     r:0