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

        int dist = 1;
        while (!q.empty()) {
            int q_size = q.size();
            for (int i = 0; i < q_size; ++i) {
                auto [r, c] = q.front();
                q.pop();
                for (auto [nr, nc] : vector<pair<int, int>>{{r - 1, c}, {r + 1, c}, {r, c - 1}, {r, c + 1}}) {
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
