# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def q_append(self, q, node):
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q, result = deque([root]), []
        while q:
            for _ in range(len(q) - 1):
                node = q.popleft()
                self.q_append(q, node)

            right_node = q.popleft()
            result.append(right_node.val)
            self.q_append(q, right_node)
        
        return result
