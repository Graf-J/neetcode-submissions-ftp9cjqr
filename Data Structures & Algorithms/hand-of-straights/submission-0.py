class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Base-Case
        if len(hand) % groupSize:
            return False

        # Fill Frequency Dictionary
        num_freq = {}
        for card in hand:
            num_freq[card] = num_freq.get(card, 0) + 1

        # Iterate through Groups
        while len(num_freq) > 0:
            group_ctr = 1
            pivot_card = next(iter(num_freq.items()))[0] # Get some card in O(1)
            num_freq[pivot_card] -= 1
            if num_freq[pivot_card] == 0:
                del num_freq[pivot_card]

            # Move Left
            current_card = pivot_card - 1
            while group_ctr < groupSize and current_card in num_freq:
                num_freq[current_card] -= 1
                if num_freq[current_card] == 0:
                    del num_freq[current_card]
                current_card -= 1
                group_ctr += 1

            # Move Right
            current_card = pivot_card + 1
            while group_ctr < groupSize and current_card in num_freq:
                num_freq[current_card] -= 1
                if num_freq[current_card] == 0:
                    del num_freq[current_card]
                current_card += 1
                group_ctr += 1

            if group_ctr < groupSize:
                return False

        return True


# Time-Complexity:  O(N)
# Space-Complexity: O(N)


# [1,2,2,3,3,4,4,5]

# {
#     1: 1,
#     2: 2,
#     3: 2,
#     4: 2,
#     5: 1
# }