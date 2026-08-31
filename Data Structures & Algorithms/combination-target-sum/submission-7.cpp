class Solution {
private:
    void dfs(int i, int sum, int target, vector<int>& nums, vector<int>& subset, vector<vector<int>>& result) {
        if (sum == target) {
            result.push_back(subset);
            return;
        }
        if (i == nums.size() || sum > target) return;

        subset.push_back(nums[i]);
        dfs(i, sum + nums[i], target, nums, subset, result);
        subset.pop_back();
        dfs(i + 1, sum, target, nums, subset, result);
    }

public:
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        vector<vector<int>> result;
        vector<int> subset;
        dfs(0, 0, target, nums, subset, result);
        return result;
    }
};



                   