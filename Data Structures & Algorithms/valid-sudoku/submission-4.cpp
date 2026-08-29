class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<int> rows(9);
        vector<int> cols(9);
        vector<int> blocks(9);

        for (int r = 0; r < 9; ++r) {
            for (int c = 0; c < 9; ++c) {
                if (board[r][c] == '.') {
                    continue;
                }

                int b = (r / 3) * 3 + (c / 3);
                int num = board[r][c] - '0';

                // Row Check
                if (rows[r] & (1 << num)) {
                    return false;
                }
                rows[r] |= (1 << num);

                // Col Check
                if (cols[c] & (1 << num)) {
                    return false;
                }
                cols[c] |= (1 << num);

                // Block Check
                if (blocks[b] & (1 << num)) {
                    return false;
                }
                blocks[b] |= (1 << num);
            }
        }

        return true;
    }
};
