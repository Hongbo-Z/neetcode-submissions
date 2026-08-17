class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # sorting

        # nums.sort()
        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return nums[i]
        # return -1
        
        # HashSet
        visit = set()
        for num in nums:
            if num in visit:
                return num
            else:
                visit.add(num)
        
