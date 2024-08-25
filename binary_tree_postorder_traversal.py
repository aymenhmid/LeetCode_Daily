# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        stack = []
        current = root

        while current or stack:
            if current:
                stack.append(current)
                result.append(current.val)
                current = current.right  # Push right child first (to be processed last in reverse order)
            else:
                node = stack.pop()
                current = node.left  # Then move to left child

        return result[::-1]
