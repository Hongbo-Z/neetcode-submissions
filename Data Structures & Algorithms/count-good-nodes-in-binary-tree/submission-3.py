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
        res = 0
        queue = collections.deque([(root, float('-inf'))])
        while queue:
            node, maxValBefore = queue.popleft()
            if node.val >= maxValBefore:
                res += 1
                maxValBefore = node.val
            if node.left:
                queue.append([node.left, maxValBefore])
            if node.right:
                queue.append((node.right, maxValBefore))
        return res