import heapq

class Solution(object):
    def kClosest(self, points, k):
        pq = []
        for p in points:
            dist = p[0]**2 + p[1]**2
            if len(pq) == k:
                heapq.heappushpop(pq, (-dist, p))
            else:
                heapq.heappush(pq, (-dist, p))
        
        return [p for (dist, p) in pq] 