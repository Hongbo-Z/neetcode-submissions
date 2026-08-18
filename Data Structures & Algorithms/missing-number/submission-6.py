class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # sum1, sum2 = 0, 0
        # for i in range(len(nums)+1):
        #     sum1 += i
        # sum2 = sum(nums)

        # return sum1 - sum2

        for i in range(len(nums) + 1):
            if i not in nums:
                return i
