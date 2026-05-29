class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subSet = []
        
        def dfs(idx, subSet, total):
            if total == target:
                res.append(subSet.copy())
                return
            if idx == len(nums) or total > target:
                return
            
            subSet.append(nums[idx])
            dfs(idx, subSet, total + nums[idx])
            subSet.pop()
            dfs(idx + 1, subSet, total)
        
        dfs(0, subSet, 0)
        return res