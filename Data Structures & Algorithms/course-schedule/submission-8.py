class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = defaultdict(list)
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        visiting = set()
        def dfs(course):
            if course in visiting:
                return False
            # if course in done:
            #     return True

            visiting.add(course)
            for pre in pre_map[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course)

            pre_map[course] = []

            return True

        return all(dfs(c) for c in range(numCourses))
