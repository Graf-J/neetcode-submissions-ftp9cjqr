class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char_start_end = {}
        for i, c in enumerate(s):
            if c not in char_start_end:
                char_start_end[c] = [i, i]
            char_start_end[c][1] = i

        start, end = {}, {}
        for c, (c_start, c_end) in char_start_end.items():
            start[c_start] = c
            end[c_end] = c

        result = []
        group = set()
        group_start = 0
        for i in range(len(s)):
            if i in start:
                if len(group) == 0:
                    group_start = i
                group.add(start[i])
            if i in end:
                group.remove(end[i])

            if len(group) == 0:
                result.append(i - group_start + 1)

        return result

# Time-Complexity:  O(N)
# Space-Complexity: O(N)


# 0   x           0   
# 1   y           1
# 2               2
# 3               3   x
# 4               4   y
# 5   z           5
# 6   b           6
# 7               7   z
# 8               8
# 9               9   b
# 10  i           10  i
# 11  s           11  s
# 12  l           12  l

# group = {}
# group_start = 0
