class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # nums.sort()
        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return True
        # return False

        counts = Counter(nums)
        for value in counts.values():
            if value > 1:
                return True
        return False
        