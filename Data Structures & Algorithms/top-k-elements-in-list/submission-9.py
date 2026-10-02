class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [element[0] for element in Counter(nums).most_common(k)]






# [1, 2, 2, 2, 3, 4, 4]

# {
#     1: 1
#     2: 3
#     3: 1
#     4: 2
# }

# [[], [], [], [], [], [], []] (same length -> take care about freq-1 indexing)

# [[1, 3], [4], [2], [], [], [], []]