class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # Option:1

        # counter_s = collections.defaultdict(int)
        # counter_t = collections.defaultdict(int)
        # for i in range(len(s)):
        #     counter_s[s[i]] += 1
        #     counter_t[t[i]] += 1
        # return counter_s == counter_t

        # Option:2
        counter_s = collections.Counter(s)
        counter_t = collections.Counter(t)

        return counter_s == counter_t
        