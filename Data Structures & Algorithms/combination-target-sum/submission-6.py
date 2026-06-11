class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(path, i, cur_sum):
            if cur_sum == target:
                result.append(path.copy())
                return
            if i == len(nums) or cur_sum > target:
                return

            path.append(nums[i])
            dfs(path, i, cur_sum + nums[i])
            path.pop()
            dfs(path, i + 1, cur_sum)

        dfs([], 0, 0)
        return result





# [2, 5, 6, 9]

#           /       \
#          2        []
#      /       \
#    2,2         2
#  /     \      /  \
# 2,2,2  2,2   2,5  2