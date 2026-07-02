class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()

        adj = defaultdict(list)
        for src, dst in tickets:
            adj[src].append([dst, False])

        result = []

        def dfs(src):
            result.append(src)

            if len(result) == len(tickets) + 1:
                return True

            for i, (neighbor, visited) in enumerate(adj[src]):
                if visited:
                    continue

                adj[src][i][1] = True

                if dfs(neighbor):
                    return True

                adj[src][i][1] = False

            result.pop()
            return False

        dfs("JFK")
        return result