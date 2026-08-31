# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = list()
        curr = head
        while curr:
            node.append(curr)
            curr = curr.next
        
        removeIdx = len(node) - n
        if removeIdx == 0:
            return head.next

        node[removeIdx - 1].next = node[removeIdx].next
        return head