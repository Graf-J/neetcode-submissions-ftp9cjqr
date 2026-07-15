class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        
        memo = {}
        def dfs(i: int, remaining: int):
            if i == len(nums) or remaining < 0:
                return False
            if remaining == 0:
                return True
            if (i, remaining) in memo:
                return memo[(i, remaining)]

            memo[(i, remaining)] = (
                dfs(i + 1, remaining) or
                dfs(i + 1, remaining - nums[i])
            )
            return memo[(i, remaining)]

        return dfs(0, s // 2)



    
#                           1                       
#             1,2                     1
#     1,2,3          1,2          1,3     1
# 1,2,3,4  1,2,3 1,2,4   1,2  1,3,4  1,3  1,4
