class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2 != 0:
            return False
        target = total / 2

        # dp = set()
        # dp.add(0)
        dp = {0}

        for num in nums:
            dp_copy = dp.copy()
            for item in dp:
                if item + num == target:
                    return True
                else:
                    dp_copy.add(item + num)
            dp = dp_copy
        return False
        
                