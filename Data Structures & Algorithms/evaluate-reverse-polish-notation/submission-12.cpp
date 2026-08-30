class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> s;
        for (const auto& token : tokens) {
            if (token == "+") {
                int second = s.top();
                s.pop();
                int first = s.top();
                s.pop();
                s.push(first + second);
            } else if (token == "-") {
                int second = s.top();
                s.pop();
                int first = s.top();
                s.pop();
                s.push(first - second);
            } else if (token == "*") {
                int second = s.top();
                s.pop();
                int first = s.top();
                s.pop();
                s.push(first * second);
            } else if (token == "/") {
                int second = s.top();
                s.pop();
                int first = s.top();
                s.pop();
                s.push(first / second);
            } else {
                s.push(stoi(token));
            }
        }

        return s.top();
    }
};
