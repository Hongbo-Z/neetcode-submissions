class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for s in strs:
            string = ''.join(sorted(s))
            d[string].append(s)
        return list(d.values())