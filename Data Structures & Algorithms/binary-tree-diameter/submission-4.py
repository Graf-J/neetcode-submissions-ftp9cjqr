# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0

            nonlocal max_diameter
            max_left = dfs(node.left)
            max_right = dfs(node.right)
        
            max_diameter = max(max_diameter, max_left + max_right)

            return 1 + max(max_left, max_right)

        dfs(root)
        return max_diameter
