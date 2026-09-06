class Solution:
    def num2digits(self, n: int) -> deque[int]:
        if n == 0:
            return deque([0])

        digits = deque()
        while n > 0:
            digits.appendleft(n % 10)
            n //= 10

        return digits
        

    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1 and n not in visited:
            visited.add(n)
            digits = self.num2digits(n)
            n = sum(map(lambda x: x**2, digits))
        
        return n == 1


# 100

# 100 % 10 = 0
# 100 // 10 = 10

# 10 % 10 = 0
# 10 // 10 = 1

# 1 % 10 = 1
# 1 // 10 = 0