class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subSet = []
        candidates.sort()

        def dfs(idx, total):
            if total == target:
                res.append(subSet.copy())
                return
            
            if idx == len(candidates) or total > target:
                return
            
            subSet.append(candidates[idx])
            dfs(idx + 1, total + candidates[idx])
            subSet.pop()
            while idx + 1 < len(candidates) and candidates[idx+1] == candidates[idx]:
                idx += 1
            dfs(idx + 1, total)
        dfs(0, 0)
        return res