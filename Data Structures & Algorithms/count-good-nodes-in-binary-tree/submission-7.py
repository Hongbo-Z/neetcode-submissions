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
        stack = [[root, - float('inf')]] # [node, max_val_befor_cur_node]
        while stack:
            node, maxVal = stack.pop()
            if node.val >= maxVal:
                res += 1
                maxVal = node.val
            if node.left:
                stack.append([node.left, maxVal])
            if node.right:
                stack.append([node.right, maxVal])
        return res