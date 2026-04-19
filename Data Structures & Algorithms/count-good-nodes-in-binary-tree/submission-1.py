# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result, stack = 0, [(root, root.val)]

        while stack:
            node, max_val = stack.pop()
            if node.val >= max_val:
                result += 1

            new_max = max(max_val, node.val)
            if node.left:
                stack.append((node.left, new_max))
            if node.right:
                stack.append((node.right, new_max))

        return result