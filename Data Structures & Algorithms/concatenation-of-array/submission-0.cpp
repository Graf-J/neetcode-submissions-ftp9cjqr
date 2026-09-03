class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> result;
        for (int i = 0; i < 2 * nums.size(); ++i) {
            result.push_back(nums[i % nums.size()]);
        }
        return result;
    }
};