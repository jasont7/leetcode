class Solution(object):
    def islandPerimeter(self, grid):
        R, C = len(grid), len(grid[0])
        P = 0
        
        def dfs(r, c):
            nonlocal P
            
            grid[r][c] = -1
            
            if r+1 >= R or grid[r+1][c] == 0: P += 1
            if r-1 <  0 or grid[r-1][c] == 0: P += 1
            if c+1 >= C or grid[r][c+1] == 0: P += 1
            if c-1 <  0 or grid[r][c-1] == 0: P += 1

            if r-1 >= 0 and grid[r-1][c] == 1: dfs(r-1, c)
            if c-1 >= 0 and grid[r][c-1] == 1: dfs(r, c-1)
            if r+1 <  R and grid[r+1][c] == 1: dfs(r+1, c)
            if c+1 <  C and grid[r][c+1] == 1: dfs(r, c+1)
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    dfs(r, c)
        
        return P