# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_potential = float("-inf")
        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            max_pot_left = dfs(root.left)
            max_pot_right = dfs(root.right)
            
            nonlocal max_potential
            potential = root.val + max(0, max_pot_left) + max(0, max_pot_right)
            max_potential = max(max_potential, potential)

            return root.val + max(max(0, max_pot_left), max(0, max_pot_right))

        dfs(root)
        return max_potential
