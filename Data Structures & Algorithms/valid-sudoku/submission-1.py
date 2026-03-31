class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, col = [set() for _ in range(9)], [set() for _ in range(9)]
        box = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                # Placeholder
                if board[i][j] == ".":
                    continue

                # Row
                if board[i][j] in row[i]:
                    return False
                row[i].add(board[i][j])
                
                # Column
                if board[i][j] in col[j]:
                    return False
                col[j].add(board[i][j])

                # Box
                if board[i][j] in box[i // 3][j // 3]:
                    return False
                box[i // 3][j // 3].add(board[i][j])

        return True
                
