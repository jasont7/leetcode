from functools import cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        @cache
        def DP(m, n):
            if m == 1 and n == 1:
                return 1
            
            if m == 1:
                return DP(m, n-1)
            if n == 1:
                return DP(m-1, n)

            return DP(m, n-1) + DP(m-1, n)
        
        return DP(m, n)