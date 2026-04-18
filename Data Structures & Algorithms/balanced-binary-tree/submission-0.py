# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        max_diff = 0
        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            nonlocal max_diff
            max_diff = max(max_diff, abs(left - right))
            return 1 + max(left, right)

        dfs(root)
        return max_diff <= 1

