class Solution:
    def numDecodings(self, s: str) -> int:
        # DP Top down
        memo = {}
        res = 0
        def dfs(i):
            if i == len(s): # if this decoding path can reach the end, then we get 1 valid decoding path
                return 1
            if s[i] == "0":
                return 0
            if i in memo:
                return memo[i]
                
            # for one digit case
            res = dfs(i+1)

            # for two digit case
            if ((i+1) < len(s) and (s[i] =="1" or s[i] == "2" and s[i+1] < "7")):
                res += dfs(i+2)
            memo[i] = res
            return res
        return dfs(0)

            
            
                