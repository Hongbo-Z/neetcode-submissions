class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # DP bottom up
        # dp = [[1]*n for i in range(m)]
        
        # for i in range(m - 2, -1, -1):
        #     for j in range(n - 2, -1, -1):
        #         dp[i][j] = dp[i+1][j] + dp[i][j+1]
        # return dp[0][0]

        # DP optimized
        row = [1]*n
        for i in range(m-1):
            new_row = [1]*n
            for j in range(n-2, -1, -1):
                new_row[j] = row[j] + new_row[j+1]
            row = new_row
        return row[0]
            
            