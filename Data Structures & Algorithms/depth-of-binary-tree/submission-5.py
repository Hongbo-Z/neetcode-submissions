# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # BFS
        # queue = collections.deque([root])
        # count = 0
        # while queue:
        #     for _ in range(len(queue)):
        #         node = queue.popleft()
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     count += 1
        # return count

        maxleft = self.maxDepth(root.left)
        maxright = self.maxDepth(root.right)
        return 1 + max(maxleft, maxright)



            