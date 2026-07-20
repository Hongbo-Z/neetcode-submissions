class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # d = dict(nums)
        # return len(d) < len(nums)

        # counts = Counter(nums)
        # for num in counts:
        #     if counts[num] > 1:
        #         return True
        # return False

        counts = collections.defaultdict(int)
        for num in nums:
            counts[num] += 1
            if counts[num] > 1:
                return True
        return False
        