class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def dfs(path, n_open, n_closed):
            if n_open == n_closed == n:
                result.append("".join(path))
                return
            if n_open > n or n_closed > n_open:
                return

            path.append("(")
            dfs(path, n_open + 1, n_closed)
            path.pop()

            path.append(")")
            dfs(path, n_open, n_closed + 1)
            path.pop()

        dfs([], 0, 0)
        return result






#             /          \
#             (           -
#            /     \
#         ((        ()
#       /   \      /  \
#    (((    (()
#    / \     / \
#   -  ((() (()(