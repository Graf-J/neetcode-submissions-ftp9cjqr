# Can also be solved using DFS

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for crs, pre in prerequisites:
            indegree[crs] += 1
            adj[pre].append(crs)

        q = deque([c for c in range(numCourses) if indegree[c] == 0])

        finish = 0
        while q:
            course = q.popleft()
            finish += 1
            for c in adj[course]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    q.append(c)

        return finish == numCourses