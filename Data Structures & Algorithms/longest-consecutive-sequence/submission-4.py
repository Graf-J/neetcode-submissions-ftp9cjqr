class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        seq_starts = []
        for num in nums:
            if num - 1 not in nums_set:
                seq_starts.append(num)

        max_seq_len = 0
        for num in seq_starts:
            ctr = 1
            while num + ctr in nums_set:
                ctr += 1
            max_seq_len = max(max_seq_len, ctr)

        return max_seq_len
