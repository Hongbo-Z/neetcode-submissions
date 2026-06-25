class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        def helper(nums):
            if not nums:
                return 0
            if len(nums) == 1:
                return nums[0]

            n = len(nums)
            pd = [0]*n
            pd[0] = nums[0]
            pd[1] = max(nums[0], nums[1])
            for i in range(2, n):
                pd[i] = max(pd[i-1], pd[i-2]+nums[i])
            return pd[n-1]

        return max(helper(nums[1:]), helper(nums[:-1]))
    
       

        
