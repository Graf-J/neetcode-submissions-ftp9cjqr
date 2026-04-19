# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result, stack = 1, [(root, root.val)]
        while stack:
            node, max_val = stack.pop()
            if node.left:
                if node.left.val >= max_val:
                    result += 1
                stack.append((node.left, max(max_val, node.left.val)))
            if node.right:
                if node.right.val >= max_val:
                    result += 1
                stack.append((node.right, max(max_val, node.right.val)))
            
        return result