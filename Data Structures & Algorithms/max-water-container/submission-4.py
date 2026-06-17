class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Solution 1: Brute force
        mArea = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                area = (j - i) * min(heights[i], heights[j])
                mArea = max(mArea, area)
        return mArea