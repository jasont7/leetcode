import heapq

class Solution(object):
    def kClosest(self, points, k):
        def dist(p):
            return p[0]**2 + p[1]**2
        
        pq = []
        for p in points:
            #print(-dist(p))
            heapq.heappush(pq, (dist(p), p))  # neg bc min-heap
        
        return [heappop(pq)[1] for _ in range(k)]
        # for i in range(k):
        #     res.append(heappop(pq)[1])
        # return res