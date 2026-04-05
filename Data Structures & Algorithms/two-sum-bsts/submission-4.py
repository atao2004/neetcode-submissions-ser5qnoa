# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        lookup = {}
        def store(node):
            if not node:
                return 
            lookup[target - node.val] = node.val
            store(node.left)
            store(node.right)
        
        def inorder(node):
            if not node:
                return False
            if node.val in lookup:
                return True
            return (inorder(node.left) or inorder(node.right))
        store(root1) 
        return (inorder(root2))