# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = collections.deque([(root, - float("inf"))]) # (curr_node, maxVal_befor_crr_node)
        res = 0
        while q:
            node, maxVal = q.popleft()
            if node.val >= maxVal:
                res += 1
                maxVal = max(maxVal, node.val)
            if node.left:
                q.append((node.left, maxVal))
            if node.right:
                q.append((node.right, maxVal))
        return res