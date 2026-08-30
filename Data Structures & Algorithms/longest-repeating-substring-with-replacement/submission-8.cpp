class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_map<char, int> m;
        int max_seq_len = 0;
        int max_freq = 0;
        int l = 0;
        for (int r = 0; r < s.size(); ++r) {
            m[s[r]]++;
            max_freq = max(max_freq, m[s[r]]);
            int window_len = r - l + 1;
            if (window_len - max_freq > k) {
                m[s[l]]--;
                l++;
            }
            max_seq_len = max(max_seq_len, r - l + 1);
        } 

        return max_seq_len;
    }
};


// s = "AAABABB"
//        l
//            r

// max_freq = 4
// m = {
//     A: 3
//     B: 3
// }


// s = "XYYX"
//      l
//         r

// max_freq = 2
// m = {
//     X: 2
//     Y: 2
// }

// r - l + 1 = 4