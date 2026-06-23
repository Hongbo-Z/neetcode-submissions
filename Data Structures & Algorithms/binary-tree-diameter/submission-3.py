# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(curr): # claculate the height of the node
            if not curr:
                return 0
            heightLeft = dfs(curr.left)
            heightRight = dfs(curr.right)
            self.res = max(self.res, heightLeft + heightRight)
            return max(heightLeft, heightRight) + 1
        dfs(root)
        return self.res
