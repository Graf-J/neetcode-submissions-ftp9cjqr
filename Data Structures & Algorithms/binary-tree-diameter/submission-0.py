# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        def dfs(root: TreeNode):
            nonlocal max_diameter
            if not root:
                return 0

            max_depth_left = dfs(root.left)
            max_depth_right = dfs(root.right)

            max_diameter = max(max_diameter, max_depth_left + max_depth_right)
            return max(max_depth_left + 1, max_depth_right + 1)

        dfs(root)
        return max_diameter


