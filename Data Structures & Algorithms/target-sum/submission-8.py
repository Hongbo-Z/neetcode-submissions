class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}    
        def dfs(i, total):
            # All numbers have been assigned + or -
            if i == len(nums):
                return 1 if total == target else 0

            if (i, total) in dp:
                return dp[(i, total)]

            # Two choices for nums[i]:
            # 1. add nums[i]
            # 2. subtract nums[i]
            add = dfs(i + 1, total + nums[i])
            subtract = dfs(i + 1, total - nums[i])

            dp[(i, total)] = add + subtract

            return add + subtract

        return dfs(0, 0)

                
