class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subSet = []
        
        def dfs(idx, total):
            if total == target:
                res.append(subSet.copy())
                return
            if idx == len(nums) or total > target:
                return
            subSet.append(nums[idx])
            dfs(idx, total + nums[idx])
            subSet.pop()
            dfs(idx + 1, total)
        
        dfs(0, 0)
        return res