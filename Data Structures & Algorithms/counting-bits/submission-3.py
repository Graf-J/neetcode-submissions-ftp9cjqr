class Solution:
    def countBits(self, n: int) -> List[int]:
        memo = {}
        def dfs(num: int) -> int:
            if num == 0:
                return 0
            if num in memo:
                return memo[num]

            msb = math.floor(math.log2(num))
            memo[num] =  1 + dfs(num - 2**msb)
            return memo[num]

        result = []
        for i in range(n + 1):
            result.append(dfs(i))

        return result
        


# 4  3  2  1
# 8, 4, 2, 1

# log2(7) = floor(3.77) = 3


                # (4)
                # (3)
                # (2)
                # (1)
                # (0)



# 0000    0

# 0001    1

# 0010    1
# 0011    2

# 0100    1
# 0101    2
# 0110    2
# 0111    3

# 1000    1
# 1001    2
# 1010    2
# 1011    3
# 1100    2
# 1101    3
# 1110    3
# 1111    4