class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for a, b in prerequisites:
            adj[a].append(b)
            indegree[b] += 1

        q = deque(i for i in range(numCourses) if indegree[i] == 0)

        completed = 0
        while q:
            course = q.popleft()
            completed += 1
            for neighbour in adj[course]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    q.append(neighbour)

        return completed == numCourses