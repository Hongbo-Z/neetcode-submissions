class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        m, n = len(grid), len(grid[0])

        def change(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != '1':
                return 
            else:
                grid[i][j] = "0"
                change(i + 1, j)
                change(i - 1, j)
                change(i, j + 1)
                change(i, j - 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    change(i, j)
                    count += 1
        
        return count
       
             
