class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            ss = ''.join(sorted(s))
            groups[ss] = groups[ss] + [s] if ss in groups else [s]
        return groups.values()