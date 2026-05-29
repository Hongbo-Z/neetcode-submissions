# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None # An empty linked list is represented by None, not [].

        for i in range(1, len(lists)):
            lists[i] = self.merge(lists[i - 1], lists[i])
        return lists[-1]
    
    def merge(self, l1:Optional[ListNode], l2:Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = ListNode(l1.val)
                l1 = l1.next
            else:
                curr.next = ListNode(l2.val)
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next
        
        
