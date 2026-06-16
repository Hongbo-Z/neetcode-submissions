class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter_s = collections.defaultdict(int)
        counter_t = collections.defaultdict(int)

        for i in range(len(s)):
            counter_s[s[i]] += 1
            counter_t[t[i]] += 1
        return counter_s == counter_t