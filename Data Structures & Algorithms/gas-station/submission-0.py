class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = (g - c  for _ in range(2) for g, c in zip(gas, cost))
        i = 0
        start = 0
        cur_gas = 0
        while i < 2 * len(gas) - 1:
            d = next(diff)
            cur_gas += d
            if cur_gas < 0:
                start = i + 1
                cur_gas = 0
            i += 1

        return -1 if start >= len(gas) else start








# gas =  [1,2,3,4]
# cost = [2,2,4,1]
#        [-1,0,-1,3]

# i = 5
# start = 3
# cur_gas = 3
# d = -1



# gas =  [1,2,3]
# cost = [2,3,2]
#        [-1,-1,1]



# [-1, 7, -3, -5, 2, 2, 2, 2]
