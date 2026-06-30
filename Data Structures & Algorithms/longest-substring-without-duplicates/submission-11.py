class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        sub_set = set()
        maxL = 0
        while r < len(s):
            while s[r] in sub_set:
                sub_set.remove(s[l])
                l += 1
            sub_set.add(s[r])
            maxL = max(maxL, r - l + 1)
            r += 1
        return maxL
