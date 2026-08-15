class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
            
        dp = set() # record all possible subset summation we can make using the numbers we have processed so far.
        dp.add(0) # if we choose nothing, the sum is 0.
        # the above two lines can be replace with: dp = {0}

        target = total // 2 # using the floor division to get the integer

        for i in range(len(nums)):
            next_dp = dp.copy()
            for item in dp:
                next_dp.add(item + nums[i])
            dp = next_dp
        return target in dp
            