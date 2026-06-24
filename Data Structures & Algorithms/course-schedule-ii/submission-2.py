class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for a, b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1

        q = deque((node for node in range(numCourses) if indegree[node] == 0))

        result = []
        while q:
            node = q.popleft()
            result.append(node)
            for course in adj[node]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    q.append(course)

        return result if len(result) == numCourses else []
            