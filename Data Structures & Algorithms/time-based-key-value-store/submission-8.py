from collections import defaultdict

Item = namedtuple("Item", ["ts", "value", "existing_keys"])

class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        l, r = 0, len(self.store[key])
        while l < r:
            m = (l + r) // 2
            if self.store[key][m][0] <= timestamp:
                result = self.store[key][m][1]
                l = m + 1
            else:
                r = m

        return result




    


# [1, 2, 3, [4], 5, 6]
