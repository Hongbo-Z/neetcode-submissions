class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # P = sum of nums with + sign
        # N = sum of nums with - sign

        # P - N = target
        # P + N = total
        # 2P = (target + total) -> P = (target + total) // 2

        # The problem reformulated to count the num of subset to total up to P

        total = sum(nums)
        if target > total:
            return 0
        if (total + target) % 2 != 0:
            return 0 

        P = (total + target) // 2 

        dp = [0]*(P + 1)
        dp[0] = 1

        for num in nums:
            for t in range(P, num -1, -1):
                dp[t] += dp[t - num]
        return dp[P]
