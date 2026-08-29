class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> m;
        for (int i = 0; i < nums.size(); ++i) {
            if (m.contains(nums[i])) {
                return vector<int>{m[nums[i]], i};
            }
            m[target - nums[i]] = i;
        }

        return vector<int>{-1, -1};
    }
};

