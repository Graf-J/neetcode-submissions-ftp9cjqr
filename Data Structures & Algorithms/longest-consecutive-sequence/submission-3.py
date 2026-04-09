class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        start_nums = []
        for num in nums:
            if num - 1 not in nums_set:
                start_nums.append(num)

        max_len = 0
        for start_num in start_nums:
            i = 1
            while start_num + i in nums_set:
                i += 1
            max_len = max(max_len, i)

        return max_len