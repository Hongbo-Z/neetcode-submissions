class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub, currSum = nums[0], 0

        for num in nums:
            # currSum = max(num, currSum + num)
            if currSum < 0:
                currSum = 0
            currSum += num
            maxSub = max(maxSub, currSum)
        return maxSub