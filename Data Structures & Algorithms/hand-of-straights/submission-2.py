class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Base-Case
        if len(hand) % groupSize:
            return False

        num_freq = {}
        for card in hand:
            num_freq[card] = 1 + num_freq.get(card, 0)
        
        heap = list(num_freq.keys())
        heapq.heapify(heap)
        while heap:
            start_card = heap[0]
            for i in range(start_card, start_card + groupSize):
                if i not in num_freq:
                    return False
                num_freq[i] -= 1
                if num_freq[i] < 0:
                    return False
                if num_freq[i] == 0 and heapq.heappop(heap) != i:
                    return False

        return True





# [1,2,2,3,3,4,4,5]

# {
#     1: 1,
#     2: 2,
#     3: 2,
#     4: 2,
#     5: 1
# }