# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        flag = True
        if not root:
            return []
        queue = deque()
        queue.append(root)
        while queue:
            arr = deque()
            for i in range(len(queue)):
                node = queue.popleft()
                if flag:
                    arr.append(node.val)
                else:
                    arr.appendleft(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            flag = not flag
            res.append(arr)
        return res

