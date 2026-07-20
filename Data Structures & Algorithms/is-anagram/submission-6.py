class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # return Counter(s) == Counter(t)
        counts_s = collections.defaultdict(int)
        counts_t = collections.defaultdict(int)

        for i in range(len(s)):
            counts_s[s[i]] += 1
            counts_t[t[i]] += 1
        return counts_s == counts_t