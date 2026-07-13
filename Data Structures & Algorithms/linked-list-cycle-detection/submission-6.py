# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = set()
        tail = head
        while tail:
            if tail in s:
                return True
            else:
                s.add(tail)
                tail = tail.next
        return False
