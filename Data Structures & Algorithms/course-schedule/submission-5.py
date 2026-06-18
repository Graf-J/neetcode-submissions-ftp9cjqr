class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = defaultdict(list)
        for a, b in prerequisites:
            pre_map[b].append(a)

        visiting = set()
        done = set()
        def dfs(course):
            if course in done:
                return True
            if course in visiting:
                return False

            visiting.add(course)
            for pre in pre_map[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course)

            done.add(course)

            return True

        return all(dfs(c) for c in range(numCourses))
