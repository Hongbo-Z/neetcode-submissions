class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxArea = 0

        def dfs(r, c, area):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c]==0:
                return
            else:
                grid[r][c] = 0
                area[0] += 1
                dfs(r + 1, c, area)
                dfs(r - 1, c, area)
                dfs(r, c + 1, area)
                dfs(r, c - 1, area)  
        
        for r in range(rows):
            for c in range(cols):
                area = [0] # list is mutable
                dfs(r, c, area)
                maxArea = max(maxArea, area[0])
        return maxArea