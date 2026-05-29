class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, columns  = len(matrix), len(matrix[0])

        dp = [[0]*(columns+1) for _ in range(rows+1)]
        maxLen = 0
        for r in range(rows - 1, -1, -1):
            for c in range(columns - 1, -1 ,-1):
                if matrix[r][c] == "1":
                    dp[r][c] = 1 + min(dp[r+1][c], dp[r][c+1], dp[r+1][c+1])
                maxLen = max(maxLen, dp[r][c])
        return maxLen**2
        


        