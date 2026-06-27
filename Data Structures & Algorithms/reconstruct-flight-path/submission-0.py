class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()

        adj = defaultdict(list)
        for i, (src, dst) in enumerate(tickets):
            adj[src].append((dst, i))

        used = [False] * len(tickets)
        path = []
        def dfs(src):
            path.append(src)

            if len(path) - 1 == len(tickets):
                return True

            for dst, idx in adj[src]:
                if not used[idx]:
                    used[idx] = True

                    if dfs(dst):
                        return True

                    used[idx] = False

            path.pop()
            return False

        dfs("JFK")
        return path