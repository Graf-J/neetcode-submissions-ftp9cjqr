class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        memo = {}
        def dfs(l: int, r: int) -> int:
            if l > r:
                return 0
            if (l, r) in memo:
                return memo[(l, r)]

            result = 0
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += dfs(i + 1, r) + dfs(l, i - 1)
                result = max(result, coins)

            memo[(l, r)] = result
            return result

        return dfs(1, len(nums) - 2)







# nums = 1, [4,2,3,7], 1

#                         (1,4)
#         0 + (2,4)   ()

