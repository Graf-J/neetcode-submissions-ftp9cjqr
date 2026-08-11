class Solution:
    def jump(self, nums: List[int]) -> int:
        target = len(nums) - 1
        result = 0
        l = r = 0
        while r < target:
            r_max = r + 1
            for i in range(l, r + 1):
                r_max = max(r_max, i + nums[i])
            l, r = r + 1, r_max
            result += 1
        return result



# target = 5
# [2,4,1,1,1,1]
#        l   r

# result = 2




