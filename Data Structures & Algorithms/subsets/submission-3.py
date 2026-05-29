class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Backtracking
        res = []
        subset = []
        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                # Terminate this DFS branch immediately and go back to the previous stack frame.
                return # stop recursion at a leaf and backtrack.
            subset.append(nums[i])
            dfs(i + 1)
            subset.remove(nums[i])
            dfs(i + 1)
        dfs(0)
        return res

