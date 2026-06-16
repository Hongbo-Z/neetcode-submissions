class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        res = 0

        for num in nums:
            if num - 1 not in set_nums:
                count = 1
                while num + count in set_nums:
                    count += 1
                res = max(res, count)
        return res