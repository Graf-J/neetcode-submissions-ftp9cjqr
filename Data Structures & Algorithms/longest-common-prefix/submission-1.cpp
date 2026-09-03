class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int min_str_len = strs[0].size();
        string min_str = strs[0];
        for (int i = 1; i < strs.size(); ++i) {
            if (strs[i].size() < min_str_len) {
                min_str_len = strs[i].size();
                min_str = strs[i];
            }
        }


        for (int i = 0; i < min_str_len; ++i) {
            char reference_char = strs[0][i];
            for (int j = 1; j < strs.size(); ++j) {
                if (strs[j][i] != reference_char) {
                    return strs[0].substr(0, i);
                }
            }
        }

        return min_str;
    }
};