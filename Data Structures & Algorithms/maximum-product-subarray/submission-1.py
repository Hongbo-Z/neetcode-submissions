class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # -1, 2, -3，4
        res = max(nums) # the initial largest product is the largest single num from nums
        curMax, curMin = 1, 1
        for num in nums:
            temp = curMax*num
            curMax = max(curMax*num, curMin*num, num)
            curMin = min(temp, curMin*num, num)
            res = max(res, curMax)
        return res 