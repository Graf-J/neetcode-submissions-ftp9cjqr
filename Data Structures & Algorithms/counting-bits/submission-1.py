class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        while n >= 0:
            num_ones = 0
            num = n
            while num > 0:
                num_ones += num & 1
                num >>= 1
            result.append(num_ones)
            n -= 1

        return list(reversed(result))
