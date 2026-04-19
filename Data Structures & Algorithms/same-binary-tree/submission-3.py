# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Both Trees have no Node (Terminal Nodes)
        if p is q is None:
            return True

        # Only one Tree has a Node (One Tree Terminal)
        if p is None or q is None or p.val != q.val:
            return False

        # Both Trees p and q defenitely exist
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)



        # values_equal = p.val == q.val
        # if p.left or q.left:
        #     values_equal = values_equal and self.isSameTree(p.left, q.left)
        # if p.right or q.right:
        #     values_equal = values_equal and self.isSameTree(p.right, q.right)

        # return values_equal
