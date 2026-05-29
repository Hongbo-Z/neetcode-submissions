class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return nums
        elif len(nums)==1:
            return nums[0]
        else:
            return max(self.subRob(nums[1:]), self.subRob(nums[:-1]))
        
    def subRob(self, nums):
        rob1, rob2 = 0, 0
        for num in nums:
            temp = max(num+rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2