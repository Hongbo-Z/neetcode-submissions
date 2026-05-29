class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # if not nums:
        #     return [[]]
        res = []
        def dfs(i, subSet, total):
            if total == target:
                res.append(subSet.copy())
                return
            if i >= len(nums) or total > target:
                return

            subSet.append(nums[i])
            dfs(i, subSet, total + nums[i])
            subSet.pop()
            dfs(i + 1, subSet, total)
        dfs(0, [], 0)
        return res
