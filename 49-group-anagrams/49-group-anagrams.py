class Solution(object):
    def groupAnagrams(self, strs):
        groups = {}
        for st in strs:
            sst = ''.join(sorted(st))
            if sst in groups:
                groups[sst].append(st)
            else:
                groups[sst] = [st]
        
        return [groups[key] for key in groups]