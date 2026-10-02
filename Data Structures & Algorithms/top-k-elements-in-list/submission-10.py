class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = {}
        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1

        freq_nums = [[] for _ in range(len(nums))]
        for num, freq in num_freq.items():
            freq_nums[freq - 1].append(num)

        result = []
        for numbers in reversed(freq_nums):
            for num in numbers:
                if len(result) == k:
                    break
                result.append(num)
            if len(result) == k:
                break

        return result





# [1, 2, 2, 2, 3, 4, 4]

# {
#     1: 1
#     2: 3
#     3: 1
#     4: 2
# }

# [[], [], [], [], [], [], []] (same length -> take care about freq-1 indexing)

# [[1, 3], [4], [2], [], [], [], []]