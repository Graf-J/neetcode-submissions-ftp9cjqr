class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1

        freq_map_sorted = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)

        result = []
        for num, freq in freq_map_sorted:
            result.append(num)
            if len(result) == k:
                break

        return result