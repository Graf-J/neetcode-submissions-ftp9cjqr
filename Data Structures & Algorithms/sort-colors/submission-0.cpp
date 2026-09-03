class Solution {
public:
    void sortColors(vector<int>& nums) {
        int r = 0;
        int g = 0;
        int b = 0;
        for (auto num : nums) {
            if (num == 0) {
                r++;
            } else if (num == 1) {
                g++;
            } else {
                b++;
            }
        }

        for (int i = 0; i < nums.size(); ++i) {
            if (r > 0) {
                nums[i] = 0;
                r--;
            } else if (g > 0) {
                nums[i] = 1;
                g--;
            } else {
                nums[i] = 2;
                b--;
            }
        }
    }
};







// [2, 2, 0, 1, 2, 0, 1, 2]
//  l                    
//                    r