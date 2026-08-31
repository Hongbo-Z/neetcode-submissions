# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        store = []
        curr = head
        while curr:
            store.append(curr)
            curr = curr.next
        
        i, j = 0, len(store) - 1
        while i < j:
            store[i].next = store[j]
            i += 1
            store[j].next = store[i]
            j -= 1
        store[i].next = None


        