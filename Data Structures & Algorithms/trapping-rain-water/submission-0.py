class Solution:
    def trap(self, height: List[int]) -> int:
        # Two pointers with tricks!!! 
        res = 0
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l]) # update the leftMax befor calculate the trap, the same for the rightMax
                res += leftMax - height[l] # we actually skip the idx:0 as it can't trap water, the same for rightmost
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res        