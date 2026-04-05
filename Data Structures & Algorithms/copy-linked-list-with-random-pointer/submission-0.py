"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        lookup = {}
        def copy(node):
            if not node:
                return 
            new = Node(node.val)
            lookup[node] = new
            new.next = copy(node.next)
            new.random = lookup.get(node.random)
            return new
        return copy(head)