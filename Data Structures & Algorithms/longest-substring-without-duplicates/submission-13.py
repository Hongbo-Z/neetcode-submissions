class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l, r = 0, 1
        res = 1
        
        while r < len(s):
            while s[r] in s[l:r]:
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res