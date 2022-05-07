class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        
        def dfsGetArea(r, c):
            area = 1
            grid[r][c] = -1  # set to seen
            
            if r+1 < R and grid[r+1][c] == 1: area += dfsGetArea(r+1, c)
            if c+1 < C and grid[r][c+1] == 1: area += dfsGetArea(r, c+1)
            if r-1 >= 0 and grid[r-1][c] == 1: area += dfsGetArea(r-1, c)
            if c-1 >= 0 and grid[r][c-1] == 1: area += dfsGetArea(r, c-1)
            
            return area
        
        maxArea = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    area = dfsGetArea(r, c)
                    maxArea = max(area, maxArea)
                    
        return maxArea