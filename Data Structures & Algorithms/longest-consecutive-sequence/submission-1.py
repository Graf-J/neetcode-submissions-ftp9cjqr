class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_seq_len = 0
        nums_set = set(nums)
        for num in nums:
            if num - 1 in nums_set:
                continue

            seq_ctr = 1
            current_num = num
            while current_num + 1 in nums_set:
                seq_ctr += 1
                current_num += 1
            max_seq_len = max(max_seq_len, seq_ctr)

        return max_seq_len


            
            
        
        

        