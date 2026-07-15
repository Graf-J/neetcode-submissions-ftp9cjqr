import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for num in nums:
            if not dp or dp[-1] < num:
                dp.append(num)
                continue
            i = bisect.bisect_left(dp, num)
            dp[i] = num

        return len(dp)









nums = [9,1,4,2,3,3,7]
dp = [9]
dp = [1]
dp = [1,4]
dp = [1,2]
dp = [1,2,3]
dp = [1,2,3]
dp = [1,2,3,7]