class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums = [1, 0, -2, 3] ->[0, -6, 0, 0]
        res = [0] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res   

        
