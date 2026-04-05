class Solution:
    def solve(self, board: List[List[str]]) -> None:
        queue= deque()
        visited=set()
        ROWS = len(board)
        COLS = len(board[0])
        def bfs(row, col):
            # queue.append((r,c))
            # visited.add((row,col))
            directions=[[0,1],[1,0],[-1,0],[0,-1]]
            while queue:
                r,c = queue.popleft()
                if board[r][c] == "O":
                    board[r][c] = "M"
                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc
                    if 0<=new_r<ROWS and 0<=new_c<COLS and  board[new_r][new_c] == "O":
                        queue.append((new_r, new_c))
                        # visited.add((row,col))
        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or r == ROWS-1 or c == 0 or c == COLS-1) and (board[r][c] == 'O'):
                    queue.append((r,c))
                    bfs(r,c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                    
                elif board[r][c] == 'M':
                    board[r][c] = 'O'
        


