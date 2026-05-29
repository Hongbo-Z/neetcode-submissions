class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # "zxyxzxyz"

        # maxLen = 0
        # for i in range(len(s)):
        #     charSet = set()
        #     for j in range(i, len(s)):
        #         if s[j] in charSet:
        #             break
        #         else:
        #             charSet.add(s[j])
        #     maxLen = max(maxLen,len(charSet))
        # return maxLen

        # Sliding window
        # l, r = 0, 0
        # maxLen = 0
        # charSet = set()
        # while r < len(s):
        #     while s[r] in charSet:
        #         charSet.remove(s[l])
        #         l += 1
        #     charSet.add(s[r])
        #     maxLen = max(maxLen, r - l +1)
        #     r += 1
        # return maxLen

        l, r = 0, 0
        maxLen = 0
        charDict = {}
        for r in range(len(s)):
            if s[r] in charDict:
                l = max(charDict[s[r]]+1,l)
            charDict[s[r]] = r
            maxLen = max(maxLen, r -l + 1)
        return maxLen
            
            



            