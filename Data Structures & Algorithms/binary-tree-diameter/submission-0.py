# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # DFS with recursive
        res = 0

        def dfs(curr): # calculate the height
            nonlocal res
            if not curr:
                return 0
            leftHeight = dfs(curr.left)
            rightHeight = dfs(curr.right)
            res = max(res, leftHeight + rightHeight)
            return 1 + max(leftHeight, rightHeight)
        dfs(root)
        return res
            


