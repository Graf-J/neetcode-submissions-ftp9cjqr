class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        target = s // 2

        dp = {0}
        for num in nums:
            dp_tmp = set()
            for current_sum in dp:
                if current_sum == target:
                    return True
                dp_tmp |= {current_sum, current_sum + num}
            dp = dp_tmp

        return False

