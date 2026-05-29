# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Method 1: Brute force with BFS
        # l = []
        # stack = [root]
        # while stack:
        #     node = stack.pop()
        #     if not node:
        #         continue
        #     l.append(node.val)
        #     stack.append(node.left)
        #     stack.append(node.right)
        # l.sort()
        # return l[k-1]

        # Method 2: Inorder Traversal with DFS
        # l = []
        # def dfs(node):
        #     if not node:
        #         return
        #     dfs(node.left)
        #     l.append(node.val)
        #     dfs(node.right)
        # dfs(root)
        # return l[k-1]

        # Method 3: Iterative DFS
        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right


            