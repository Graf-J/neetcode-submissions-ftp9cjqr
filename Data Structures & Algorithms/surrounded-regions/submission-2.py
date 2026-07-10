class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW, COL = len(board), len(board[0])

        q = deque()
        for c in range(1, COL):
            if board[0][c] == "O":
                q.append((0, c))
                board[0][c] = "X"
        for r in range(1, ROW):
            if board[r][COL - 1] == "O":
                q.append((r, COL - 1))
                board[r][COL - 1] = "X"
        for c in range(0, COL - 1):
            if board[ROW - 1][c] == "O":
                q.append((ROW - 1, c))
                board[ROW - 1][c] = "X"
        for r in range(0, ROW - 1):
            if board[r][0] == "O":
                q.append((r, 0))
                board[r][0] = "X"


        visited = set()
        while q:
            r, c = q.popleft()
            visited.add((r, c))
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if (
                    0 <= nr < ROW and
                    0 <= nc < COL and
                    board[nr][nc] == "O"
                ):
                    board[nr][nc] = "X"
                    q.append((nr, nc))

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "X" and (r, c) in visited:
                    board[r][c] = "O"
