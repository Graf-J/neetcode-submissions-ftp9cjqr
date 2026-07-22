class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        memo = {}
        def dfs(l: int, r: int) -> int:
            if r < l:
                return 0
            if (l, r) in memo:
                return memo[(l, r)]

            max_coins = 0
            for i in range(l, r + 1):
                max_coins = max(max_coins, dfs(l, i - 1) + nums[l - 1] * nums[i] * nums[r + 1] + dfs(i + 1, r))

            memo[(l, r)] = max_coins
            return max_coins

        return dfs(1, len(nums) - 2)













# [1 | 4, 2, 3, 7 | 1]

#                                 (1, 4)
#     max((1,0) + 1*4*1 + (2,4)   ,   (1,1) + 1*2*1 + (3,4)  ,  ...)
#                                  0 + 1*4*2 + 0