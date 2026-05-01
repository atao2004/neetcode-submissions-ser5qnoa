class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        mins = 0
        queue = deque()
        fresh = 0

        # rot all fruits
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append((r, c))
                if grid[r][c] == 1:
                    fresh +=1
        directions = [[0,1],[0,-1],[-1,0],[1, 0]]

        while queue and fresh > 0:
            for _ in range(len(queue)): # represent 'waves' of converted fresh->rotten fruits
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if nr in range(m) and nc in range(n) and grid[nr][nc] == 1:
                        fresh -= 1
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
            mins += 1
        #check for unrotted fruits:
        # for r in range(m):
        #     for c in range(n):
        #         if grid[r][c] == 1:
        #             return -1
        return mins if fresh == 0 else -1