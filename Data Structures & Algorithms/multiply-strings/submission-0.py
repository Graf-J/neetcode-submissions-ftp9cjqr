class Solution:
    def str2digits(self, num: str) -> list[int]:
        digits = []
        for c in num:
            digits.append(ord(c) - ord("0"))

        return digits

    def digits2str(self, digits: list[int]) -> str:
        s = []
        for digit in digits:
            s.append(chr(ord("0") + digit))

        return "".join(s)

    def digits2num(self, digits: list[int]) -> int:
        num = 0
        for i in range(len(digits)):
            num *= 10
            num += digits[i]

        return num

    def num2digits(self, num: int) -> list[int]:
        digits = []
        while num > 0:
            digits.append(num % 10)
            num //= 10

        return digits[::-1]

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        n1 = self.digits2num(self.str2digits(num1))
        n2 = self.digits2num(self.str2digits(num2))

        result = n1 * n2
        return self.digits2str(self.num2digits(result))



# 123

# 123 % 10 = 3
# 123 // 10 = 12

# 12 % 10 = 2
# 12 // 10 = 1

# 1 % 10 = 1
# 1 // 10 = 0
