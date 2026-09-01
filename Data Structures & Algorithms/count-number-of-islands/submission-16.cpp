class Solution {
private:
    void dfs(int r, int c, vector<vector<char>>& grid) {
        const int ROWS = grid.size();
        const int COLS = grid[0].size();

        if (
            r < 0 or r >= ROWS or
            c < 0 or c >= COLS or
            grid[r][c] == '0'
        ) return;

        grid[r][c] = '0';
        for (auto [nr, nc] : vector<pair<int, int>>{{r + 1, c}, {r - 1, c}, {r, c + 1}, {r, c - 1}}) {
            dfs(nr, nc, grid);
        }
    }

public:
    int numIslands(vector<vector<char>>& grid) {
        const int ROWS = grid.size();
        const int COLS = grid[0].size();

        int num_islands = 0;
        for (int r = 0; r < ROWS; ++r) {
            for (int c = 0; c < COLS; ++c) {
                if (grid[r][c] == '1') {
                    dfs(r, c, grid);
                    num_islands++;
                }
            }
        }

        return num_islands;
    }
};
