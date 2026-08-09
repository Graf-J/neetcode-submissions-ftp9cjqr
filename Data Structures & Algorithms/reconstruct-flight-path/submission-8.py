class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)
        
        adj = defaultdict(list)
        for src, dst in tickets:
            adj[src].append(dst)

        result = []
        stack = ["JFK"]
        while stack:
            city = stack[-1]
            if adj[city]:
                stack.append(adj[city].pop())
            else:
                result.append(stack.pop())

        return result[::-1]

        
