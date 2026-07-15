class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def dfs(p: int, i: int) -> int:
            if i == n:
                return 0
            if (p, i) in memo:
                return memo[(p, i)]

            lis = dfs(p, i + 1)
            if p == -1 or nums[i] > nums[p]:
                lis = max(lis, 1 + dfs(i, i + 1))

            memo[(p, i)] = lis
            return lis

        return dfs(-1, 0)




# nums = [9,1,4,2,3,3,7]

#                         O
#             9                   []
        
    