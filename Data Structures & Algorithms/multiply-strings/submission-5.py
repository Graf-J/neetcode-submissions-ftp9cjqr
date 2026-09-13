class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n = len(num1) + len(num2)
        result = [0] * n

        for idx_1, i1 in enumerate(range(len(num1) - 1, -1, -1)):
            for idx_2, i2 in enumerate(range(len(num2) - 1, -1, -1)):
                pos = n - idx_1 - idx_2 - 1

                product = int(num1[i1]) * int(num2[i2])

                total = result[pos] + product
                result[pos] = total % 10
                carry_val = total // 10

                carry_idx = pos - 1

                while carry_val > 0:
                    total = result[carry_idx] + carry_val
                    result[carry_idx] = total % 10
                    carry_val = total // 10
                    carry_idx -= 1

        out = "".join(map(str, result)).lstrip("0")
        return out or "0"

            
                
















# 123
# 456

# [0, 0, 0, 0, 0, 0]

# 3 * 6 = 18
# 2 * 6 = 12
# 1 * 6 = 6

# [0, 0, 0, 7, 3, 8]

# 3 * 5 = 15
# 2 * 5 = 10
# 1 * 5 = 5

# [0, 0, 6, 8, 8, 8]

# 3 * 4 = 
# 2 * 4 = 
# 1 * 4 =



