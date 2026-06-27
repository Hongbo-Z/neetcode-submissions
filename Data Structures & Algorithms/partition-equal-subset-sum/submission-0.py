class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        dp = set()
        dp.add(0)
        target = sum(nums)/2

        for i in range(len(nums) - 1, -1, -1):
            next_dp = dp.copy()
            for item in dp:
                next_dp.add(item + nums[i])
            dp = next_dp
        return target in dp
            