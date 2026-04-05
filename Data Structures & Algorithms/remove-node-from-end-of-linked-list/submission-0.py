# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        if not head:
            return
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        # index to remove
        i = len(nodes) - n
        if i == 0:
            return head.next
        if i + 1 < len(nodes):
            nodes[i-1].next = nodes[i+1]
        else:
            nodes[i-1].next = None
                    
        return head
            
