class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number_freq = [0] * 2001
        for num in nums:
            number_freq[num + 1000] += 1

        freq_number = [[] for _ in range(len(nums) + 1)]
        for idx, freq in enumerate(number_freq):
            num = idx - 1000
            freq_number[freq].append(num)

        result = []
        for numbers in reversed(freq_number):
            if k == 0:
                break

            for num in numbers:
                result.append(num)
                k -= 1

        return result

# 1)
# List: [1, 2, 2, 3, 3, 3]
# Num -> Freq: [0, 1, 2, 3, 0, 0] # -1000 - 1000
# Freq -> Num: [[0, 4, 5], [1], [2], [3], [], []] # 0 - len(nums)
# Iterate from behind
# O(N + 2001 + L)

# 2)
# List: [1, 2, 2, 3, 3, 3]
# Num -> Freq: [0, 1, 2, 3, 0, 0] # -1000 - 1000
# Min-Heap with length k: [(3, 3), (2, 2)]

# O(N + 2001*log(k))
