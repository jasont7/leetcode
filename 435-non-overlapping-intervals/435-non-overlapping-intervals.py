class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        cnt, end = 0, None
        for i in sorted(intervals, key=lambda x: x[1]):
            if cnt == 0 or i[0] >= end:
                end = i[1]
                cnt += 1
        return len(intervals) - cnt 
