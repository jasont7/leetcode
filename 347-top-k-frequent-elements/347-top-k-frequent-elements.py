import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        
        pq = []
        for n in freq:
            if len(pq) == k:
                heapq.heappushpop(pq, (freq[n], n))
            else:
                heapq.heappush(pq, (freq[n], n))
                
        return [n for (freq, n) in pq]