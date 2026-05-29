# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # # Brute force: Time O(n), Space O(n)
        # node = []
        # curr = head
        # while curr:
        #     node.append(curr)
        #     curr = curr.next

        # removeIdx = len(node) - n
        # if removeIdx == 0:
        #     return head.next

        # node[removeIdx -1].next = node[removeIdx].next
        # return head
        
        # # Iteration (Two Pass): Time O(n), Space(1) 
        # count = 0
        # curr = head
        # while curr:
        #     count += 1
        #     curr = curr.next
        # removeIdx = count - n
        # if removeIdx == 0:
        #     return head.next
        # temp = head
        # idx = 0
        # while idx < removeIdx -1:
        #     temp = temp.next
        #     idx += 1
        # temp.next = temp.next.next
        # return head       

        # two pointers
        p1 = p2 = head
        for _ in range(n):
            p2 = p2.next
        # if p2 is None: which is equal to the below
        if not p2: 
            return head.next

        while p2.next:
            p1 = p1.next
            p2 = p2.next
        p1.next = p1.next.next
        return head
        



        