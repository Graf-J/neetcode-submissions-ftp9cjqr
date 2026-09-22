class CountSquares:
    def __init__(self):
        self.d = defaultdict(int)
        self.cols = defaultdict(set)

    def add(self, point: List[int]) -> None:
        x, y = point

        self.d[(x, y)] += 1
        self.cols[x].add(y)

    def count(self, point: List[int]) -> int:
        q_x, q_y = point
        ctr = 0
        for y in self.cols[q_x]:
            if y == q_y:
                continue
                
            side = abs(q_y - y)
            left = self.d[(q_x, y)] * self.d[(q_x - side, q_y)] * self.d[(q_x - side, y)]
            right = self.d[(q_x, y)] * self.d[(q_x + side, q_y)] * self.d[(q_x + side, y)]
            ctr += (left + right)

        return ctr


#   q_x - side, y     y, q_x


#   q_x - side, q_y   q_x, q_y


# d = {
#     (1, 1): 1
#     (1, 2): 1
#     (2, 2): 1
# }

# cols = {
#     1: set[1, 2]
#     2: set[2]
# }

# count([2, 1])

# 1) Iterate over cols[2]
#     d = abs(y1 - y2)
# 2.1) Check to the right
#     Multiply d_0 * d_1 * d_2
# 2.2) Check to the left
#     Multiply d_0 * d_1 * d_2

# 3) Return sum






