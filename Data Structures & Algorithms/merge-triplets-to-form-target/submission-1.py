class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        current = [0, 0, 0]
        for a, b ,c in triplets:
            if (
                max(current[0], a) <= target[0] and
                max(current[1], b) <= target[1] and
                max(current[2], c) <= target[2]
            ):
                current = [max(current[0], a), max(current[1], b), max(current[2], c)]

        return current == target


