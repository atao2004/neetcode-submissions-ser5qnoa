# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def countGood(root, max_so_far):
            if not root:
                return 0
            if root.val >= max_so_far:
                return 1 + (countGood(root.left, root.val) + countGood(root.right, root.val))
            else:
                return (countGood(root.left, max_so_far) + countGood(root.right, max_so_far))
        if not root:
            return 0
        return countGood(root, root.val)