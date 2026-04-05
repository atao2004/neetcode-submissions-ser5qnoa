# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = deque()
        q.append(root)
        found_null = False
        while q:
            node = q.popleft()
            if not node.left and node.right:
                return False
            if (node.left  or node.right) and found_null:
                return False
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            else:
                found_null = True
        return True
            
            
