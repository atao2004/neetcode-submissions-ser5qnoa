# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        def binarySearch(node, target2):
            if not node:
                return False
            if node.val == target2:
                return True
            if node.val > target2:
                return binarySearch(node.left, target2)
            else:
                return binarySearch(node.right, target2)
        def findNode(node):
            if not node:
                return False
            if binarySearch(root2, target-node.val):
                return True
            return findNode(node.left) or findNode(node.right)
        return findNode(root1)
