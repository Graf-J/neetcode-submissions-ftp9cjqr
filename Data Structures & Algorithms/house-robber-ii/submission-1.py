class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
 
        # Iteration 1
        dp = [0] * (n - 1)
        dp[-2:] = [max(nums[-3:-1]), nums[-2]]
        for i in range(n - 4, -1, -1):
            dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])
        best_1 = dp[0]

        # Iteration 2
        dp = [0] * (n - 1)
        dp[-2:] = [max(nums[-2:]), nums[-1]]
        for i in range(n - 3, 0, -1):
            dp[i - 1] = max(nums[i] + dp[i + 1], dp[i])
        best_2 = dp[0]

        return max(best_1, best_2)




'''
[2, 9, 8, 3, 6]

# Iteration 1
[?, ?, 8, 3]
    ^
? = max(9 + 3, 8) = 12

[?, 12, 8, 3]
 ^
? = max(2 + 8, 12) = 12

best_1 = 12

# Iteration 2
   [?, ?, 6, 6]
          ^
? = max(8 + 6, 6) = 14

   [?, 14, 6, 6]
    ^
? = max(9 + 6, 14) = 15

best_2 = 15

return max(12, 15) = 15
'''





