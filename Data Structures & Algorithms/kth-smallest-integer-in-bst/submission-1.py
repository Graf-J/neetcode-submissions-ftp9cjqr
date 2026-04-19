# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ctr, result = 0, None
        def inorder_traversal(node: Optional[TreeNode]):
            if not node:
                return

            nonlocal ctr, result
            inorder_traversal(node.left)
            ctr += 1
            if ctr == k:
                result = node.val

            inorder_traversal(node.right)


        inorder_traversal(root)
        return result
