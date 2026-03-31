class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for number in nums:
            hashmap[number] = 1 + hashmap.get(number, 0)

        sorted_hashmap = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)

        return [val[0] for val in sorted_hashmap[:k]]

        