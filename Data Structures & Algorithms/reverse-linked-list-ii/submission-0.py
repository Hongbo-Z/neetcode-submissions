# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        leftPre, curr = dummy, head

        for _ in range(left - 1):
            leftPre, curr = curr, curr.next
        
        pre = None
        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp
        
        leftPre.next.next = curr
        leftPre.next = pre
        return dummy.next


        
