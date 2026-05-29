class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(i, subSet):
            if i == len(nums):
                res.append(subSet.copy())
                return
            subSet.append(nums[i])
            dfs(i + 1, subSet)
            subSet.pop()
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            dfs(i + 1, subSet)
        dfs(0, [])
        return res