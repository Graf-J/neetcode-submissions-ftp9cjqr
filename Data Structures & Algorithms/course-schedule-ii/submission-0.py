class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for crs, pre in prerequisites:
            indegree[crs] += 1
            adj[pre].append(crs)

        q = deque([c for c in range(numCourses) if indegree[c] == 0])

        result = []
        while q:
            course = q.popleft()
            result.append(course)
            for c in adj[course]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    q.append(c)

        return result if len(result) == numCourses else []