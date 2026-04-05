class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        visit = set()
        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visit.add((r,c))
            area =1
            directions=[[0, 1],[1,0],[0,-1],[-1,0]]
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc
                    if new_r in range(rows) and new_c in range(cols) and (new_r, new_c) not in visit and grid[new_r][new_c] ==1:
                        visit.add((new_r, new_c))
                        q.append((new_r, new_c))
                        area +=1
            return area
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(bfs(r, c), max_area)
        return max_area
        
                        



        
