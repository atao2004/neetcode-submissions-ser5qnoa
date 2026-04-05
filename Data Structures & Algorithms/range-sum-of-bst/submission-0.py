# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def getSum(node, low, high):
            if not node:
                return 0
            if node.val < low or node.val > high:
                return getSum(node.left, low, high) + getSum(node.right, low, high)
            else:
                return node.val + getSum(node.left, low, high) + getSum(node.right, low, high)
        return getSum(root, low, high)