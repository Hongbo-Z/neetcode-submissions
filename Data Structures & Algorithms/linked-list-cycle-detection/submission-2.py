# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        map = {}
        while head:
            if head in map.keys():
                return True
            map[head] = head.next
            head = head.next
        return False 