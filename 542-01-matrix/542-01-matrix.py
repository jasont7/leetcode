from collections import deque

class Solution(object):
    def updateMatrix(self, grid):
        R, C = len(grid), len(grid[0])
        
        q = deque()
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    q.append((r, c))
                else:
                    grid[r][c] = 1000000
        
        while q:
            r, c = q.popleft()
            
            # update adjacent cells
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                rr, cc = r + dr, c + dc
                if rr >= R or rr < 0 or cc >= C or cc < 0:
                    continue
                if grid[rr][cc] <= grid[r][c]:
                    continue
                
                grid[rr][cc] = 1 + grid[r][c]
                q.append((rr, cc))
        
        return grid