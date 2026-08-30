class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> result(temperatures.size());
        stack<pair<int, int>> s;
        for (int i = 0; i < temperatures.size(); ++i) {
            if (s.empty() || temperatures[i] <= s.top().first) {
                s.push({temperatures[i], i});
            } else {
                while (!s.empty() && temperatures[i] > s.top().first) {
                    result[s.top().second] = i - s.top().second;
                    s.pop();
                }
                s.push({temperatures[i], i});
            }
        }

        return result;
    }
};








// [30,38,30,36,35,40,28]

// result: [1,4,1,2,1,0,0]

// stack: (38, 1) (36, 3) (35,4) (40,5)