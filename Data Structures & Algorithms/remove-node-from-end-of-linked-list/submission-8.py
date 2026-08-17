# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 让两个指针始终相隔 n 个节点，这样当 p2 到达链表末尾时，p1 正好停在待删除节点的前一个位置。
        p1, p2 = head, head
        for _ in range(n):
            p2 = p2.next
        
        if not p2:
            return head.next

        while p2.next:
            p1 = p1.next
            p2 = p2.next
        p1.next = p1.next.next
        return head