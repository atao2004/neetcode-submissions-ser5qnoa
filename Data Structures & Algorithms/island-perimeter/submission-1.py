class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        queue = deque()
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        perim = 0

        m = len(grid)
        n = len(grid[0])
        def bfs(r, c):
            nonlocal perim
            queue.append((r, c))
            visited.add((r,c))

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if nr not in range(m) or nc not in range(n)or grid[nr][nc] == 0:
                        perim += 1
                    elif grid[nr][nc] == 1 and (nr,nc) not in visited:
                        queue.append((nr,nc))
                        visited.add((nr,nc))
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and (r,c) not in visited:
                    bfs(r,c)
        return perim
