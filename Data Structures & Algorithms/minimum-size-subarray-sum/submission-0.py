class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        curSum = 0
        res = float('inf')
        while r < len(nums):
            curSum += nums[r]
            while curSum >= target:
                res = min(res, r - l + 1)
                curSum -= nums[l]
                l += 1
            r += 1
        return 0 if res == float('inf') else res

