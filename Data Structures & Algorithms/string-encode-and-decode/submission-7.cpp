class Solution {
public:
    string encode(vector<string>& strs) {
        string encodedStr;
        for (const auto& s : strs) {
            encodedStr += to_string(s.size()) + '#' + s;
        }
        return encodedStr;
    }

    vector<string> decode(string s) {
        vector<string> result;
        int i = 0;
        while (i < s.size()) {
            int j = i;
            while (s[j] != '#') {
                j++;
            }
            int numChars = stoi(s.substr(i, j - i));
            
            result.push_back(s.substr(j + 1, numChars));
            i = j + numChars + 1;
        }

        return result;
    }
};



// ["Hello", "World"]
// -> "5#Hello5#World"

// i = 7
// j = 8
// numChars = 5