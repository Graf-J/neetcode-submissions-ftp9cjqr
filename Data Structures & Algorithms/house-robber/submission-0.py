class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def dfs(i):
            if i == len(nums):
                return 0
            if i >= len(nums) - 2:
                return nums[i]
            if i in cache:
                return cache[i]
            
            val = nums[i] + max(dfs(i + 2), dfs(i + 3))
            cache[i] = val
            return val

        dfs_1 = 0
        dfs_0 = dfs(0)
        if len(nums) > 1:
            dfs_1 = dfs(1)

        return max(dfs_1, dfs_0)




# [2, 9, 8, 3, 6]
#           ^  ^     Have to rob one of these
# -> i = 4

# [2, 9, 8, 3, 6]
#     ^  ^          Have to rob one of these


#                 O
#         2               9
#     8       3       3       6
# 6                        
