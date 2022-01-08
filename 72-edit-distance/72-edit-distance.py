from functools import cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        @cache
        def DP(A, B, n, m):
            if min(n, m) == 0:
                return max(n, m)
            
            if A[n-1] == B[m-1]:
                return DP(A[:n-1], B[:m-1], n-1, m-1)
            
            return min(
                1 + DP(A[:n-1], B[:m], n-1, m),
                1 + DP(A[:n], B[:m-1], n, m-1),
                1 + DP(A[:n-1], B[:m-1], n-1, m-1)
            )
        
        return DP(word1, word2, len(word1), len(word2))