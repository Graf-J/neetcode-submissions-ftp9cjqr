from collections import defaultdict

class TimeMap:
    def __init__(self):
        self.key_ts = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_ts[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        latest_entry = ""
        l, r = 0, len(self.key_ts[key])
        while l < r:
            m = (l + r) // 2
            if self.key_ts[key][m][0] <= timestamp:
                latest_entry = self.key_ts[key][m][1]
                l = m + 1
            else:
                r = m
        return latest_entry
                
        
