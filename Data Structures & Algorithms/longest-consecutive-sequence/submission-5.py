class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        seq_start_nums = []
        for num in nums:
            if num - 1 not in nums_set:
                seq_start_nums.append(num)

        longest_seq = 0
        for seq_start_num in seq_start_nums:
            i = 1
            while seq_start_num + i in nums_set:
                i += 1
            longest_seq = max(i, longest_seq)

        return longest_seq


# Space-Complexity: O(N)
# Time-Complexity: O(N)

# nums: [2,20,4,10,3,4,5]
# nums_set: {2,20,10,3,4,5} -> O(N)

# seq_start_nums = [2, 20, 10] -> O(N)

# longest_seq = 4
# seq_start_num = 10
# i = 1 -> O(N)

# return 4
