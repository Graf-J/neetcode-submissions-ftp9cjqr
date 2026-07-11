class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)

        adj = defaultdict(list)
        for src, dst in tickets:
            adj[src].append(dst)

        result = []
        stack = ["JFK"]
        while stack:
            if adj[stack[-1]]:
                stack.append(adj[stack[-1]].pop())
            else:
                result.append(stack.pop())

        return result[::-1]

        
