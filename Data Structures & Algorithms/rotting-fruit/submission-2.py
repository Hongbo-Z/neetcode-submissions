class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        time, fresh = 0, 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        while q and fresh > 0:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r in range(len(grid)) and c in range(len(grid[0])) and grid[r][c] == 1:
                        grid[r][c] = 2
                        q.append((r,c))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1

