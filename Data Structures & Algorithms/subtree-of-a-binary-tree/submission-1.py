# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def treesMatch(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.treesMatch(p.left, q.left) and self.treesMatch(p.right, q.right)

    def isSubtree(self, root, subRoot):
        q = deque([root])
        while q:
            node = q.popleft()
            if node and self.treesMatch(node, subRoot):
                return True
            if node:
                q.append(node.left)
                q.append(node.right)
        return False
                