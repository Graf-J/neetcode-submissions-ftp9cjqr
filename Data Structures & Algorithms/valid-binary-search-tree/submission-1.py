# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid(node: Optional[TreeNode], gt: int, lt: int) -> bool:
            if not node:
                return True

            return (
                (gt < node.val < lt) and 
                is_valid(node.left, gt, node.val) and 
                is_valid(node.right, node.val, lt)
            )

        return is_valid(root, float("-inf"), float("inf"))
        
