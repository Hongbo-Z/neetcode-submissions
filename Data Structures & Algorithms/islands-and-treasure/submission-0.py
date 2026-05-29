class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        while q:
            r, c = q.popleft()
            cur_dist = grid[r][c]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr < 0 or nc < 0 or nr >= rows or nc >= cols):
                    continue
                if grid[nr][nc] == INF:
                    grid[nr][nc] = cur_dist + 1
                    q.append((nr, nc))


            
        