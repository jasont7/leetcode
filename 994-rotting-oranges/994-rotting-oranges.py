from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        
        fresh_cnt = 0
        rottenQ = deque()
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    fresh_cnt += 1
                elif grid[r][c] == 2:
                    rottenQ.append((r, c))
        
        mins_passed = 0
        while rottenQ and fresh_cnt > 0:
            # process rotten oranges on the current BFS level
            for _ in range(len(rottenQ)):
                r, c = rottenQ.popleft()

                # turn all adjacent fresh organges rotten
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    rr, cc = r + dr, c + dc
                    if rr >= R or rr < 0 or cc >= C or cc < 0:
                        continue

                    if grid[rr][cc] == 1:
                        grid[rr][cc] = 2
                        fresh_cnt -= 1
                        rottenQ.append((rr, cc))
            
            # increment minutes passed after each BFS level
            mins_passed += 1
            
        return mins_passed if fresh_cnt == 0 else -1
