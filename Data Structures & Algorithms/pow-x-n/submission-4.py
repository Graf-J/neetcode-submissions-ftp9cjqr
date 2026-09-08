class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        is_neg = n < 0
        half_pow = self.myPow(x, abs(n) // 2)
        factor = x if n % 2 else 1
        if is_neg:
            return 1 / (factor * half_pow * half_pow)
        else:
            return factor * half_pow * half_pow






# 2 ** 10

#                         2**10
#                     2**5  *   2**5
#             2 * 2**2 * 2**2
#             2**1 * 2**1
#         2 * 2**0 * 2**0



#                         2**(-10)
#                     2**-5 *   2**-5
#                 2**-2 * 2**-2 * -2
#              2**-1 * 2**-1
#           2 ** 1 ** 1


#                         -2**10
#                     -2**5 * -2**5