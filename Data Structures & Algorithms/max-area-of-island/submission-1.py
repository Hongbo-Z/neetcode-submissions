class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Below using the nonlocal variable
        maxArea = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            nonlocal area # !!!
            if (r < 0 or c < 0 or r == rows or c == cols or grid[r][c] == 0):
                return 
            else:
                grid[r][c] = 0
                area += 1
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1) 
                
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = 0 # integers are immutable, it remains 0
                    dfs(r, c)
                    maxArea = max(maxArea, area)
        return maxArea
