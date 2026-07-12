class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {1: 1, 2: 2}
        for i in range(3, n + 1):
            cache[i] = cache[i - 1] + cache[i - 2]

        return cache[n]