class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # DP - Bottom up
        # dp[i] means whether the substring of s[i:] can be segmented
        dp = [False]*(len(s)+1)
        dp[len(s)] = True # empty string is valid

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if (i+len(w)) <=len(s) and s[i:i+len(w)] == w and dp[i+len(w)]:
                    dp[i] = True
        return dp[0]


        