class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for string in strs:
            s = "".join(sorted(string))   
            d[s].append(string)
        return list(d.values())