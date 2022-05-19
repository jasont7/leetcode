import heapq

class Solution(object):
    def kClosest(self, points, k):
        def dist(p):
            return p[0]**2 + p[1]**2
        
        pq = []
        for p in points:
            heapq.heappush(pq, (dist(p), p))
        
        return [heappop(pq)[1] for _ in range(k)]