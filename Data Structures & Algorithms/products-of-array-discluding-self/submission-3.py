class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums = [1, 2, 3, 4]
        # prefix = [1, 1, 2, 6]
        # postfix = [24, 12, 8, 1]

        l = len(nums)    
        res = [0] * l
        
        prefix = 1
        for i in range(l):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for j in range(l-1, -1, -1):
            res[j] *= postfix
            postfix *= nums[j]
        return res
