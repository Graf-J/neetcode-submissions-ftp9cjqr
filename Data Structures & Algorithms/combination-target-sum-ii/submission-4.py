class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def dfs(i, path, current):
            if current == target:
                result.append(path.copy())
                return
            if current > target or i >= len(candidates):
                return

            dfs(i + 1, path + [candidates[i]], current + candidates[i])
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, path, current)

        dfs(0, [], 0)
        return result