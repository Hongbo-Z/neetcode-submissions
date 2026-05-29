class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # "zxyyabc"
        
        # Brute force
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

        # Sliding window with Set
        # l, r = 0, 0
        # maxLen = 0
        # charSet = set()
        # while r < len(s):
        #     while s[r] in charSet: # this loop is used to find the index of last s[r] appear place
        #         charSet.remove(s[l]) 
        #         l += 1
        #     charSet.add(s[r])
        #     maxLen = max(maxLen, r - l +1)
        #     r += 1
        # return maxLen

        # Sliding Window with HashMap
        l, r = 0, 0
        maxLen = 0
        charDict = {} # stores the last index where each character appeared.
        for r in range(len(s)):
            if s[r] in charDict:
                l = max(l, charDict[s[r]]+1) # max is necessary here to avoid l pointer rollback
            charDict[s[r]] = r 
            maxLen = max(maxLen, r -l + 1)
        return maxLen
            
            



            