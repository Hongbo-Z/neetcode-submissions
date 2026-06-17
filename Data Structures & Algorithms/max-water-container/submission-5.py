class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Solution 1: Brute force
        # mArea = 0
        # for i in range(len(heights)):
        #     for j in range(i + 1, len(heights)):
        #         area = (j - i) * min(heights[i], heights[j])
        #         mArea = max(mArea, area)
        # return mArea

        # Solution 2: Two pointers
        l, r = 0, len(heights) - 1

        mArea = 0
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            mArea = max(mArea, area)
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return mArea
