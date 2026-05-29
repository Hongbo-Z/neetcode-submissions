class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # nums.sort()
        # for i in range(1,len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False

        # counts = Counter(nums)
        # for value in counts.values():
        #     if value > 1:
        #         return True
        # return False

        if len(set(nums)) < len(nums):
            return True
        return False
        
