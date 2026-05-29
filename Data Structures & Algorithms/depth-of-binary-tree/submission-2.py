# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        # # Method1: Recursive
        # leftDepth = self.maxDepth(root.left)
        # rightDepth = self.maxDepth(root.right)
        # return 1 + max(leftDepth, rightDepth)

        # Method2: BFS with queue
        # q = deque([root])
        # depth = 0
        # while q:
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     depth += 1
        # return depth

        # Method 3: DFS with Stack
        stack = [[root, 1]]
        res = 0
        while stack:
            node, depth = stack.pop()
            res = max(res, depth)
            if node.left:
                stack.append([node.left, depth + 1])
            if node.right:
                stack.append([node.right, depth + 1])
        return res




