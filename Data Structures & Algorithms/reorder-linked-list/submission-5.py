# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        node = list()
        dummy = head
        while dummy:
            node.append(dummy)
            dummy = dummy.next
        
        i, j = 0, len(node) -1
        while i < j:
            node[i].next = node[j]
            i += 1
            node[j].next = node[i]
            j -= 1
        node[i].next = None
