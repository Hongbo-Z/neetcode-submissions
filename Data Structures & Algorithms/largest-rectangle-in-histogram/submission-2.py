class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        heights.append(0)
        for i in range(len(heights)):
            
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                left = stack[-1] if stack else -1
                res = max(res, (i - left - 1)*h)

            stack.append(i)

        return res

            