class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(permutation: list[int], visited: set[int]) -> None:
            if len(permutation) == len(nums):
                result.append(permutation.copy())

            for i in range(len(nums)):
                if i in visited:
                    continue

                permutation.append(nums[i])
                visited.add(i)
                dfs(permutation, visited)
                permutation.pop()
                visited.remove(i)

        dfs([], set())
        return result
    






    #                     ()
    #     1               2               3
    # 2       3       1       3       1       2