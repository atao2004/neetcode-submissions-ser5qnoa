# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root
        def getClosest(node, target):
            if not node:
                return
            nonlocal closest
            if abs(target - node.val) < abs(closest.val - target):
                closest = node
            getClosest(node.left, target)
            getClosest(node.right, target)
        getClosest(root, target)
        return closest.val
