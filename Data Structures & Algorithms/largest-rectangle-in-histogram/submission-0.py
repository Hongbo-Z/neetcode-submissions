class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 递增栈存下标，遇到更矮就结算，宽度用左右第一个更矮柱子夹出来
        # A bar’s max rectangle is formed when the first smaller bar appears on its right.
        # For each bar, how wide can it extend left and right while staying the shortest bar in that rectangle?
        
        stack = []
        res = 0
        heights.append(0)

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                left = stack[-1] if stack else -1
                width = i - left - 1
                res = max(res, h * width)
            stack.append(i)

        return res