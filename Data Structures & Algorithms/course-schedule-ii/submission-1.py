class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            indegree[a] += 1
            adj[b].append(a)

        q = deque([crs for crs in range(numCourses) if indegree[crs] == 0])

        result = []
        while q:
            crs = q.popleft()
            result.append(crs)
            for neighbor in adj[crs]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return result if len(result) == numCourses else []