# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        same = True
        def dfs(n1, n2):
            nonlocal same
            if n1 is None and n2 is None:
                return

            if n1 is None or n2 is None:
                same = False
                return

            if n1.val != n2.val:
                same = False
                return

            dfs(n1.left, n2.left)
            dfs(n1.right, n2.right)

        dfs(p, q)
        return same