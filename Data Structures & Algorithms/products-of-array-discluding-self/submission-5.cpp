class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> prefix{1};
        vector<int> suffix(nums.size(), 1);
        
        int cum_prod = 1;
        for (int i = 0; i < nums.size() - 1; ++i) {
            cum_prod *= nums[i];
            prefix.push_back(cum_prod);
        }

        cum_prod = 1;
        for (int i = nums.size() - 1; i > 0; --i) {
            cum_prod *= nums[i];
            suffix[i - 1] = cum_prod;
        }

        vector<int> result;
        for (int i = 0; i < nums.size(); ++i) {
            result.push_back(prefix[i] * suffix[i]);
        }

        return result;
    }
};








// previx =  [1,    1,    1*2, 1*2*4]
// suffix =  [2*4*6, 4*6, 6,   1    ]
