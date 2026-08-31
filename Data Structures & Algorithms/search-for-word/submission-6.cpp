class Solution {
private:
    bool dfs(const int r, const int c, int i, string& word, vector<vector<char>>& board, unordered_set<string>& visited, const size_t ROWS, const size_t COLS) {
        string s = to_string(r) + "," + to_string(c);
        if (i == word.size()) return true;
        if (
            r < 0 or r >= ROWS or
            c < 0 or c >= COLS or
            word[i] != board[r][c] or
            visited.contains(s)
        ) return false;

        visited.insert(s);
        for (const auto& [nr, nc] : vector<pair<int, int>>{{r - 1, c}, {r + 1, c}, {r, c + 1}, {r, c - 1}}) {
            if (dfs(nr, nc, i + 1, word, board, visited, ROWS, COLS)) {
                return true;
            }
        }
        visited.erase(s);
        return false;
    }

public:
    bool exist(vector<vector<char>>& board, string word) {
        const int ROWS = board.size();
        const int COLS = board[0].size();

        unordered_set<string> visited;

        for (int r = 0; r < ROWS; ++r) {
            for (int c = 0; c < COLS; ++c) {
                if (dfs(r, c, 0, word, board, visited, ROWS, COLS)) {
                    return true;
                }
            }
        }

        return false;
    }
};
