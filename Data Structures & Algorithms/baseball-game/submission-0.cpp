class Solution {
public:
    int calPoints(vector<string>& operations) {
        int sum = 0;
        stack<int> s;
        for (auto& op : operations) {
            if (op == "+") {
                int first = s.top();
                s.pop();
                int second = s.top();
                s.push(first);
                s.push(first + second);
                sum += first + second;
            } else if (op == "D") {
                s.push(s.top() * 2);
                sum += s.top();
            } else if (op == "C") {
                sum -= s.top();
                s.pop();
            } else {
                int num = stoi(op);
                sum += num;
                s.push(num);
            }
        }

        return sum;
    }
};