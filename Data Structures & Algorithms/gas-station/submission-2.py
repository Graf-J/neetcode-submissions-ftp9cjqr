class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start = total = 0
        for i, (g, c) in enumerate(zip(gas, cost)): # Only needs one iteration since because of guard I know a solution exists by the end
            total += g - c
            if total < 0:
                start = i + 1
                total = 0

        return start
