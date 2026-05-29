class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # You are asked to solve it within O(n) so, you can't lean on sort() which is O(nlogn)
        
        # HashSet
        set_nums = set(nums) # set() will enforce deduplicate operation 
        res = 0 # res used to on behalf of the current longest length

        for num in nums:
            if (num - 1) not in nums:
                count = 1
                while (num + count) in nums:
                    count += 1
                res = max(res, count) 
        return res
        