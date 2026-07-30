"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None}
        
        curr = head
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next
        
        temp = head
        while temp:
            copy = oldToCopy[temp]
            copy.next = oldToCopy[temp.next]
            copy.random = oldToCopy[temp.random]
            temp = temp.next
        return oldToCopy[head]
