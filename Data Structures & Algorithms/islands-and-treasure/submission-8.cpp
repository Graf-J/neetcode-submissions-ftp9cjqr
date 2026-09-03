class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        const int INF = pow(2, 31) - 1;
        const int ROWS = grid.size();
        const int COLS = grid[0].size();

        queue<pair<int, int>> q;
        for (int r = 0; r < ROWS; ++r) {
            for (int c = 0; c < COLS; ++c) {
                if (grid[r][c] == 0) {
                    q.push({r, c});
                }
            }
        }

        const vector<pair<int, int>> directions{
            {-1, 0},
            {1, 0},
            {0, -1},
            {0, 1}
        };

        int dist = 1;
        while (!q.empty()) {
            int q_size = q.size();
            for (int i = 0; i < q_size; ++i) {
                auto [r, c] = q.front();
                q.pop();
                for (auto [dr, dc] : directions) {
                    int nr = r + dr;
                    int nc = c + dc;
                    if (
                        nr >= 0 && nr < ROWS &&
                        nc >= 0 && nc < COLS &&
                        grid[nr][nc] == INF
                    ) {
                        grid[nr][nc] = dist;
                        q.push({nr, nc});
                    }
                }
            }
            dist++;
        }
    }
};
