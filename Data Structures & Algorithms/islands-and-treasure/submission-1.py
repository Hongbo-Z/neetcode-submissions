class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r, c])
        
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while q:
            row, col = q.popleft()
            curr_dis = grid[row][col]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if r < 0 or c < 0 or r >= rows or c >= cols:
                    continue
                if grid[r][c] == INF:
                    grid[r][c] = curr_dis + 1
                    q.append([r, c])

