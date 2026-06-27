class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        # impossible case
        if abs(target) > total:
            return 0

        # target + total must be even
        if (target + total) % 2 != 0:
            return 0

        new_target = (target + total) // 2

        dp = [0] * (new_target + 1)
        dp[0] = 1

        for num in nums:
            for s in range(new_target, num -1, -1):
                dp[s] += dp[s - num]

        return dp[new_target]