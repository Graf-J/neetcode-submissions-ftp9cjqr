class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> m{
            {')', '('},
            {']', '['},
            {'}', '{'}
        };
        stack<char> pStack;

        for (char c : s) {
            if (c == '(' || c == '[' || c == '{') {
                pStack.push(c);
            } else {
                if (pStack.empty()) {
                    return false;
                }
                if (pStack.top() != m[c]) {
                    return false;
                }
                pStack.pop();
            }
        }

        return pStack.empty();
    }
};
