# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialize(root: Optional[TreeNode]):
            if not root:
                return "N"
            return f"{root.val},{serialize(root.left)},{serialize(root.right)}"

        root_serialized = serialize(root)
        sub_root_serialized = serialize(subRoot)
        return sub_root_serialized in root_serialized