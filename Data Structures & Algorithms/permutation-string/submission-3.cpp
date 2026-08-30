class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.size() > s2.size()) {
            return false;
        }

        unordered_map<char, int> m;
        for (const auto& c : s1) {
            m[c]++;
        }

        int chars_matching = 0;
        int l = 0;
        int r = 0;
        while (r < s1.size()) {
            if (m.contains(s2[r])) {
                if (m[s2[r]] > 0) {
                    chars_matching++;
                }
                m[s2[r]]--;
            }
            r++;
        }
        if (chars_matching == s1.size()) {
            return true;
        }

        while (r < s2.size()) {
            if (m.contains(s2[r])) {
                if (m[s2[r]] > 0) {
                    chars_matching++;
                }
                m[s2[r]]--;
            }
            
            if (m.contains(s2[l])) {
                if (m[s2[l]] >= 0) {
                    chars_matching--;
                }
                m[s2[l]]++;
            }

            if (chars_matching == s1.size()) {
                return true;
            }

            l++;
            r++;
        }

        return false;
    }
};


// s2 = "lecabee"
//          l
//            r

// chars_matching = 2
// m = {
//     "a": 1
//     "b": 0
//     "c": 0
// }



// s2 = "aaabc"
//         l
//           r

// chars_matching = 3
// m = {
//     "a": 0
//     "b": 0
//     "c": 0
// }