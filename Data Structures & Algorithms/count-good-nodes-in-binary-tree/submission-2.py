# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val) -> int:
            if not node:
                return 0

            good = node.val >= max_val
            return (
                good + 
                dfs(node.left, max(node.val, max_val)) + 
                dfs(node.right, max(node.val, max_val))
            )

        return dfs(root, float("-inf"))