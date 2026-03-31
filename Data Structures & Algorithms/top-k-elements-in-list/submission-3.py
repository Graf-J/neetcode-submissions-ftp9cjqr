from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create Map: Number -> Count
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        # Create Buckets
        buckets = [[] for _ in range(len(nums))]
        for num, count in counts.items():
            buckets[count - 1].append(num)

        # Extract Result
        result = []
        for i in range(len(nums)-1, -1, -1):
            if buckets[i]:
                result.extend(buckets[i])

            if len(result) >= k:
                break

        return result
            
        