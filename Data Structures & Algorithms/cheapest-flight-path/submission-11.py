class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        costs = [float("inf")] * n
        costs[src] = 0
        for _ in range(k + 1):
            updated = False
            costs_tmp = costs.copy()
            for start, end, price in flights:
                if costs[start] + price < costs_tmp[end]:
                    updated = True
                    costs_tmp[end] = costs[start] + price

            if not updated:
                break
            costs = costs_tmp

        return -1 if costs[dst] == float("inf") else costs[dst]



# costs = [0, 200, 300, 500]

# k = 1
# costs_tmp = [0, 200, 300, 500]



