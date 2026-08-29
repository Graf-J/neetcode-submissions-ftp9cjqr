class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());

        vector<vector<int>> result;
        for (int i = 0; i < nums.size() - 2; ++i) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            
            int l = i + 1;
            int r = nums.size() - 1;
            while (l < r) {
                if (nums[i] + nums[l] + nums[r] == 0) {
                    result.push_back(vector<int>{nums[i], nums[l], nums[r]});
                    l++;
                    while (l < r and nums[l] == nums[l - 1]) {
                        l++;
                    }
                    r--;
                    while (l < r and nums[r] == nums[r + 1]) {
                        r--;
                    }
                } else if (nums[i] + nums[l] + nums[r] < 0) {
                    l++;
                } else {
                    r--;
                }
            }
        }

        return result;
    }
};




// [-4, -1, -1, 0, 1, 2]
