class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> s;
        for (const auto& num : nums) {
            s.insert(num);
        }

        vector<int> starts;
        for (const auto& num : nums) {
            if (s.find(num - 1) == s.end()) {
                starts.push_back(num);
            }
        }

        int longestSequenceLength = 0;
        for (const auto& start : starts) {
            int ctr = 1;
            int current = start;
            while (s.find(current + 1) != s.end()) {
                ctr++;
                current++;
            }
            longestSequenceLength = max(longestSequenceLength, ctr);
        }

        return longestSequenceLength;
    }
};
