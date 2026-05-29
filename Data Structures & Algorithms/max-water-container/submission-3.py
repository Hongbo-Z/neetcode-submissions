class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Brute force: Time O(n^2), Space O(1)
        # mArea = 0
        # for i in range(len(heights)):
        #     for j in range(i+1, len(heights)):
        #         area = min(heights[i], heights[j])*(j-i)
        #         mArea = max(mArea,area)
        # return mArea
        
        # Two pointer: Time O(n), Space O(1)
        mxArea = 0
        l, r = 0, len(heights) - 1
        while l < r:
            mxArea = max(mxArea, min(heights[l],heights[r])*(r-l))
            if heights[l] < heights[r]: # only move the shoter side
                l += 1
            else:
                r -= 1
        return mxArea