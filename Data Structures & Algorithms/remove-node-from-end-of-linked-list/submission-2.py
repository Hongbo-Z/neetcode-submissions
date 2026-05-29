# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Two pointers
        dumy = ListNode(0, head)
        l = r = dumy
        for _ in range(n):
            r = r.next
        while r.next:
            l = l.next
            r = r.next
        l.next = l.next.next
        return dumy.next 