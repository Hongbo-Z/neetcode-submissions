class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {} # value -> idx

        for idx, num in enumerate(nums):
            if target - num in mapping.keys():
                return [mapping[target - num], idx]
            else:
                mapping[num] = idx