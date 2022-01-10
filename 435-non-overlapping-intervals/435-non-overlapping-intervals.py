class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda i: i[1])
        
        A = []
        for i in intervals:
            if not len(A) or i[0] >= A[-1][1]:
                A.append(i)
        
        return len(intervals) - len(A) 