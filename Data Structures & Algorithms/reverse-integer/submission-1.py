class Solution:
    def reverse(self, x: int) -> int:
        MIN, MAX = -2147483648, 2147483647

        is_neg = x < 0
        x = abs(x)

        result = 0
        while x > 0:
            r = x % 10
            x //= 10

            if result > (-MIN if is_neg else MAX) // 10:
                return 0
            result *= 10

            if result > (-MIN if is_neg else MAX) - r:
                return 0
            result += r

        return -result if is_neg else result





# -123

# is_neg = True
# abs(123)

# 123 % 10 = 3
# 123 // 10 = 12

# 12 % 10 = 2
# 12 // 10 = 1

# 1 % 10 = 1
# 1 // 10 = 0



# 0 * 10 = 0
# 0 + 3 = 3

# 3 * 10 = 30
# 30 + 2 = 32

# 32 * 10 = 320
# 320 + 1 = 321

# 321 * (-1) = -321