class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2 != 0:
            return False
        target = total / 2

        dp = {0} # record all the possible subset summation we can make so far

        for num in nums:
            copy_dp = dp.copy()
            for item in dp:
                copy_dp.add(item + num)
            dp = copy_dp
        return target in dp