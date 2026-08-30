class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> m;
        int max_length = 0;
        int l = 0;
        for (int r = 0; r < s.size(); ++r) {
            if (m.find(s[r]) != m.end()) {
                l = max(l, m[s[r]] + 1);
            }
            m[s[r]] = r;
            max_length = max(max_length, r - l + 1);
        }

        return max_length;
     }
};

// max_len = 5
// s = "abcbdaebd"
//          l
//             r

// m = {
//     a: 5
//     b: 7
//     c: 2
//     d: 4
//     e: 6
// }