class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        const int ROWS = matrix.size();
        const int COLS = matrix[0].size();

        int l = 0;
        int r = ROWS * COLS - 1;
        while (l <= r) {
            int m = (l + r) / 2;
            int row = m / COLS;
            int col = m % COLS;
            if (matrix[row][col] == target) {
                return true;
            } else if (matrix[row][col] < target) {
                l = m + 1;
            } else {
                r = m - 1;
            }
        }

        return false;
    }
};
