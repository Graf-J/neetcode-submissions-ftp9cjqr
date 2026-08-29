class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> m;
        for (auto& num : nums) {
            m[num]++;
        }

        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        for (auto& [num, freq] : m) {
            pq.push(pair<int, int>{freq, num});
            if (pq.size() > k) {
                pq.pop();
            }
        }

        vector<int> result;
        while (!pq.empty()) {
            result.push_back(pq.top().second);
            pq.pop();
        }

        return result;
    }
};
