class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        result, abs_n = x, abs(n)
        while abs_n > 1:
            result *= x
            abs_n -= 1

        return result if n > 0 else 1/result

