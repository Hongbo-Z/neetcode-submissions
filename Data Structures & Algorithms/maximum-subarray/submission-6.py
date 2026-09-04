class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        r = 0
        res = max(nums)
        curSum = 0
        while r < len(nums):
            curSum += nums[r]
            res = max(res, curSum)
            if curSum < 0:
                curSum = 0
            r += 1
        return res
        