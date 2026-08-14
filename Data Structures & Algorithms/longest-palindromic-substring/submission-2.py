class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        def expand(i, j):
            nonlocal res
            while i > -1 and j < len(s) and s[i] == s[j]:
                if len(res) < j - i + 1:
                    res = s[i:j+1]  
                i -= 1
                j += 1    

        for i in range(len(s)):
            expand(i, i)
            expand(i, i+1)
        
        return res