class Solution:
    def numDecodings(self, s: str) -> int:
        # DP (Top-Down)
        pd = {len(s):1} # dp[i] = the answer for subproblem i
        def dfs(i): 
            if i in pd:
                return pd[i]
            if s[i] == "0":
                return 0
            res = dfs(i+1)
            if i+1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] < "7"):
                res += dfs(i+2)
            pd[i] = res
            return res
        return dfs(0)

        # # Recursive 
        # # dsf(i) is the number of ways to decode s[i:]
        # def dfs(i):
        #     if i == len(s):
        #         return 1
        #     if s[i] == "0":
        #         return 0
        #     # for one dight case
        #     res = dfs(i+1)
        #     # for two digits case
        #     if i+1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] < "7"):
        #         res += dfs(i+2)
        #     return res
        # return dfs(0)

        



