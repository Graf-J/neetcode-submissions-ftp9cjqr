# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(root_node: Optional[TreeNode], sub_root_node: Optional[TreeNode]) -> bool:
            if not root_node and not sub_root_node:
                return True
            if root_node is None or sub_root_node is None:
                return False

            return (
                root_node.val == sub_root_node.val and 
                dfs(root_node.left, sub_root_node.left) and 
                dfs(root_node.right, sub_root_node.right)
            )

        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None:
            return False
        return dfs(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
