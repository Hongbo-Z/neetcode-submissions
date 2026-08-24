class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = collections.defaultdict(list)
        for s in strs:
            string = "".join(sorted(s))
            group[string].append(s)
        return list(group.values())