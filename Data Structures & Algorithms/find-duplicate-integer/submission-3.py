class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # option1: Brute force: Time O(n^2) Space O(1)
        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return nums[i]
        # return -1
        
        # option2: sorting
        # nums.sort()
        # for i in range(len(nums) -1):
        #     if nums[i] == nums[i+1]:
        #         return nums[i]
        # return -1

        # hashset
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return num
        return -1
        