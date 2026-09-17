class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        dp = {0}
        target = total // 2
        for num in nums:
            dp_copy = dp.copy()
            for item in dp:
                dp_copy.add(item + num)
            dp = dp_copy
        return target in dp