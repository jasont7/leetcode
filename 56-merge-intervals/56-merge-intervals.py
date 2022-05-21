class Solution(object):
    def merge(self, intervals):
        if len(intervals) == 1: return intervals
        
        intervals.sort(key=lambda x: x[0])
        
        res = []
        cur = intervals[0]
        for i in intervals[1:]:
            if i[0] > cur[1]:
                res.append(cur)
                cur = i
            elif i[1] > cur[1]: 
                cur[1] = i[1]
        res.append(cur)
        return res