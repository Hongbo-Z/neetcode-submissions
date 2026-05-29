class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # length = len(nums)
        # res = [0]*length

        # for i in range(length):
        #     prod = 1
        #     for j in range(length):
        #         if j != i:
        #             product *= nums[j]
        #     res[i] = prod
        # return res

        l = len(nums)
        res = [0]*l

        prefix = 1
        for i in range(l):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for j in range(l-1, -1, -1):
            res[j] *= postfix
            postfix *= nums[j]
        
        return res



