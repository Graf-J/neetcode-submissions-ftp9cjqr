class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def dfs(path, num_open, num_close):
            if num_open == num_close == n:
                result.append("".join(path))
                return

            if num_open < n:
                path.append("(")
                dfs(path, num_open + 1, num_close)
                path.pop()
            if num_close < num_open:
                path.append(")")
                dfs(path, num_open, num_close + 1)
                path.pop()

        dfs([], 0, 0)
        return result