class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visit = []

        def dfs(i, j, n):
            if n == len(word):
                return True
            
            if i < 0 or j < 0 or i >= rows or j >= cols or (i, j) in visit or board[i][j] != word[n]:
                return False
            
            visit.append((i, j))
            found = (
                dfs(i + 1, j, n + 1) or
                dfs(i - 1, j, n + 1) or
                dfs(i, j + 1, n + 1) or
                dfs(i, j - 1 ,n + 1)
            )
            visit.pop()
            return found
        
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False