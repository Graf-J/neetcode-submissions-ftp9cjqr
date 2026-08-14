class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char_last_idx = {}
        for i, c in enumerate(s):
            char_last_idx[c] = i

        result = []
        start = end = 0
        for i, c in enumerate(s):
            if end < i:
                start = i
            end = max(end, char_last_idx[c])
            if i == end:
                result.append(end - start + 1)

        return result


# {
#     x: 3
#     y: 4
#     z: 7
#     b: 9
#     i: 10
#     s: 11
#     l: 12
# }
# start = 5
# end = 7
# i = 5