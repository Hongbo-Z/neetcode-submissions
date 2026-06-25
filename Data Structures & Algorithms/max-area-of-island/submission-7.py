class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c, count):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c]==0:
                return 0
                
            count[0] += 1
            grid[r][c] = 0
            dfs(r + 1, c, count)
            dfs(r - 1, c, count)
            dfs(r, c + 1, count)
            dfs(r, c - 1, count)
            return count[0] 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    count = [0] # list is mutable while integer is immutable
                    maxArea = max(maxArea, dfs(r, c, count))
        return maxArea

        
