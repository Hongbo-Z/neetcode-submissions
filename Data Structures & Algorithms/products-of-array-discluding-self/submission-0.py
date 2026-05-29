class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [0]*length

        for i in range(length):
            product = 1
            for j in range(length):
                if j != i:
                    product *= nums[j]
            res[i] = product
        return res
