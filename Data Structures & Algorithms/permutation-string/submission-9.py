class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n: return False

        counts_1 = collections.defaultdict(int)
        counts_2 = collections.defaultdict(int)

        for i in range(m):
            counts_1[s1[i]] += 1
            counts_2[s2[i]] += 1
        if counts_1 == counts_2:
            return True

        for j in range(m, n):
            counts_2[s2[j]] += 1
            counts_2[s2[j - m]] -= 1
            if counts_2[s2[j - m]] == 0:
                del counts_2[s2[j - m]]
            if counts_1 == counts_2:
                return True
        return False