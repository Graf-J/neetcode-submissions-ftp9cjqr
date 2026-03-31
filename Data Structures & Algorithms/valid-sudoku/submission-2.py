class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box_width = 3
        rows = [0] * len(board)
        cols = [0] * len(board[0])
        boxes = [0] * int((len(board) * len(board[0])) / box_width**2) 

        for i in range(len(board)):
            for j in range(len(board[0])):
                # Skip Placeholder
                if board[i][j] == ".":
                    continue

                # Validation
                bit_num = 1 << (int(board[i][j]) - 1)
                if (
                    rows[i] & bit_num or 
                    cols[j] & bit_num or 
                    boxes[(i // 3) * 3 + (j // 3)] & bit_num
                ):
                    return False

                # Updating
                rows[i] |= bit_num
                cols[j] |= bit_num
                boxes[(i // 3) * 3 + (j // 3)] |= bit_num

        return True
                
