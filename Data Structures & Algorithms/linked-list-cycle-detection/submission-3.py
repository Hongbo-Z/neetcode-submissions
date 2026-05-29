# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # HashSet
        visited = set()
        curr = head # Aviod disrupt the original liked list
        while curr:
            if curr in visited:
                return True
            visited.add(curr) 
            curr = curr.next
        return False 