# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def getSum(node, sum_so_far):
            if not node:
                return False
            sum_so_far += node.val
            if not node.right and not node.left:
                return sum_so_far == targetSum
            return (getSum(node.left, sum_so_far) or getSum(node.right, sum_so_far))
        return getSum(root, 0)
            
                

    