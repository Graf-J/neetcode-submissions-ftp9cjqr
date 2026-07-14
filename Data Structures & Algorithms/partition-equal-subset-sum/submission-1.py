class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        target = s // 2

        memo = {}
        def dfs(i: int, current_sum: int) -> bool:
            if current_sum == target:
                return True
            if i == len(nums) or current_sum > target:
                return False
            if (i, current_sum) in memo:
                return memo[(i, current_sum)]

            result = (
                dfs(i + 1, current_sum) or
                dfs(i + 1, current_sum + nums[i])
            )

            memo[(i, current_sum)] = result
            return result

        return dfs(0, 0)



    
#                           1                       
#             1,2                     1
#     1,2,3          1,2          1,3     1
# 1,2,3,4  1,2,3 1,2,4   1,2  1,3,4  1,3  1,4
