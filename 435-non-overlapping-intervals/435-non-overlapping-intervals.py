class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda i: i[1])
        
        A = [intervals[0]]
        for i in intervals[1:]:
            if i[0] >= A[-1][1]:
                A.append(i)
        
        return len(intervals) - len(A)