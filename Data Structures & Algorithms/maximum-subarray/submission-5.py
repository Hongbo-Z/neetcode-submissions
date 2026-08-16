class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub, curSub = max(nums), 0

        for num in nums:
            if curSub < 0:
                curSub = 0
            curSub += num
            maxSub = max(maxSub, curSub)
        return maxSub