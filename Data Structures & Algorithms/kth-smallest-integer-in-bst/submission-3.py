# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Recursive with DFS
        l_val = []
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            l_val.append(node.val)
            dfs(node.right)
        dfs(root)
        return l_val[k-1]
