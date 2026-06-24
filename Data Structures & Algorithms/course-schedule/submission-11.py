class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for a, b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1

        q = deque([node for node in range(numCourses) if indegree[node] == 0])

        result = []
        while q:
            prerequisite = q.popleft()
            for course in adj[prerequisite]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    q.append(course)

        return not any(indegree)