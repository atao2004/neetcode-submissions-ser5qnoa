# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        dia = 0
        def height(root3):
            if not root3:
                return 0
            return 1 + max(height(root3.left), height(root3.right))
        def dfs(root1):
            nonlocal dia
            if not root1:
                return 0
            dia = max(dia, height(root1.left) + height(root1.right))
            dfs(root1.left)
            dfs(root1.right)
        dfs(root)
        return dia
