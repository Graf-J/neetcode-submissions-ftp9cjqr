class Solution {
private:
    void dfs(int i, vector<int>& nums, vector<int>& current, vector<vector<int>>& result) {
        if (i == nums.size()) {
            result.push_back(current);
            return;
        }

        current.push_back(nums[i]);
        dfs(i + 1, nums, current, result);
        current.pop_back();
        dfs(i + 1, nums, current, result);
    }

public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> current;
        dfs(0, nums, current, result);
        return result;
    }
};



    //             (0)
    //     (1)             (1)
    // (2)     (2)     (2)     (2)