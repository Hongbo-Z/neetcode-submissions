class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]


        map = {} # value -> index

        for i, num in enumerate(nums):
            if target - num in map.keys():
                return [map[target - num], i]
            else:
                map[num] = i