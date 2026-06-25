class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subSet = []

        nums.sort()

        def dfs(idx, total):
            if total == target:
                res.append(subSet.copy())
                return

            if idx == len(nums) or total > target:
                return

            subSet.append(nums[idx])
            dfs(idx, total + nums[idx]) # Same number can be repeated used

            subSet.pop()
            dfs(idx + 1, total)
        dfs(0, 0)
        return res 
