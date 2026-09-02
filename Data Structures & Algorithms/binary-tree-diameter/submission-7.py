# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node): # calculate the max depth from current node
            nonlocal res
            if not node:
                return 0
            maxLeft = dfs(node.left)
            maxRight = dfs(node.right)
            res = max(res, maxLeft + maxRight)
            return 1 + max(maxLeft, maxRight)
        dfs(root)
        return res
