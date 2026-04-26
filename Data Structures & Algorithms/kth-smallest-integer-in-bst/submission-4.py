# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = None
        def inorder_traversal(node: Optional[TreeNode]):
            nonlocal k, result
            if not node or result is not None:
                return

            inorder_traversal(node.left)
            k -= 1
            if k == 0:
                result = node.val
            inorder_traversal(node.right)

        inorder_traversal(root)
        return result