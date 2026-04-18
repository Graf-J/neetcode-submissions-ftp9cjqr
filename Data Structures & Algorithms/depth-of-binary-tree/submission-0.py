# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def get_depth(root, depth) -> int:
            if not root:
                return depth

            max_left_depth = get_depth(root.left, depth + 1)
            max_right_depth = get_depth(root.right, depth + 1)
            return max(max_left_depth, max_right_depth)

        return get_depth(root, 0)













        # max_depth = 0
        # def depth(root: Optional[TreeNode], d: int):
        #     if root is None:
        #         return

