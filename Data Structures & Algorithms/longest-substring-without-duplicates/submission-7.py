class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        maxL = 1
        l, r = 0, 1
        
        while r < len(s):
            while s[r] in s[l:r]:
                l += 1 
            
            maxL = max(maxL, r - l +1)
            r += 1
        return maxL    
        