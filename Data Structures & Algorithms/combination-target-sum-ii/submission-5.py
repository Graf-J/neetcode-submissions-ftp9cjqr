class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        result, path = [], []
        def dfs(i: int, s: int):
            if s == target:
                result.append(path.copy())
                return
            if i == len(candidates) or s > target:
                return

            path.append(candidates[i])
            dfs(i + 1, s + candidates[i])
            path.pop()
            i += 1
            while i < len(candidates) and candidates[i - 1] == candidates[i]:
                i += 1
            dfs(i, s)

        dfs(0, 0)
        return result
            

# target = 8
# [1,2,2,4,5,6,9]
# result = []
# path = [1,2,2]


# (0,0)
# (1,1)
# (2,3)
# (3,5)

