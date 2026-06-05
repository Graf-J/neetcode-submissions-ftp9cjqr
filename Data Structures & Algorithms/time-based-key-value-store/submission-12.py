class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # timeseries = self.store[key]

        if not key in self.store:
            return ""
        if self.store[key][0][0] > timestamp:
            return ""

        l, r = 0, len(self.store[key]) - 1
        while l < r:
            m = (l + r + 1) // 2
            if self.store[key][m][0] <= timestamp:
                l = m
            else:
                r = m - 1

        return self.store[key][l][1]
