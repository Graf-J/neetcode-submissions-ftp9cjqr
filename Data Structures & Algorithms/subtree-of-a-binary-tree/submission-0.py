# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def treesMatch(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True

        if p is None or q is None or p.val != q.val:
            return False

        result = True
        if p.left or q.left:
            result = result and self.treesMatch(p.left, q.left)
        if p.right or q.right:
            result = result and self.treesMatch(p.right, q.right)
        return result

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = deque([root])
        while q:
            node = q.popleft()
            if self.treesMatch(node, subRoot):
                return True
            if node:
                q.append(node.left)
                q.append(node.right)

        return False
                