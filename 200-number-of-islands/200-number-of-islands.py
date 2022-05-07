class Solution(object):
    def numIslands(self, grid):
        R, C = len(grid), len(grid[0])
        
        def dfsFlip(r, c):
            if grid[r][c] == '1':
                grid[r][c] = '0'
                if r-1 >= 0: dfsFlip(r-1, c)
                if r+1 < R: dfsFlip(r+1, c)
                if c-1 >= 0: dfsFlip(r, c-1)
                if c+1 < C: dfsFlip(r, c+1)
        
        islands = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1':
                    dfsFlip(r, c)
                    islands += 1
        
        return islands