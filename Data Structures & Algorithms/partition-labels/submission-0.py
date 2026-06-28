class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastCharIdx = {}
        for i, c in enumerate(s):
            lastCharIdx[c] = i

        res = []
        count, end = 0, 0
        for i in range(len(s)):
            count += 1
            end = max(end, lastCharIdx[s[i]])
            if i == end:
                res.append(count)
                count = 0
        return res

