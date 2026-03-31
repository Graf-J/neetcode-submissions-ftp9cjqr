class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for number in nums:
            hashmap[number] = 1 + hashmap.get(number, 0)

        frequencies = [[] for _ in range(len(nums))]
        for num, num_freq in hashmap.items():
            frequencies[num_freq - 1].append(num)

        result = []
        for freq_idx in range(len(nums) - 1, -1, -1):
            for num in frequencies[freq_idx]:
                result.append(num)
                if len(result) == k:
                    return result
        