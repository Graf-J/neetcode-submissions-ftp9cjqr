class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int max_freq = 0;
        int max_val = 0;
        unordered_map<int, int> m;
        for (auto num : nums) {
            m[num]++;
            if (m[num] > max_freq) {
                max_freq = m[num];
                max_val = num;
            }

            if (max_freq > nums.size() / 2) break;
        }

        return max_val;
    }
};