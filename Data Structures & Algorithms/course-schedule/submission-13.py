class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for a, b in prerequisites:
            adj[a].append(b) # "a" depends on "b"
            indegree[b] += 1

        q = deque(c for c in range(numCourses) if indegree[c] == 0)

        ctr = 0
        while q:
            c = q.popleft()
            ctr += 1
            for neighbor in adj[c]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return ctr == numCourses