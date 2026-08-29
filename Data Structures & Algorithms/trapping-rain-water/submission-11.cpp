class Solution {
public:
    int trap(vector<int>& height) {
        int l = 0;
        int r = height.size() - 1;

        int lMax = 0;
        int rMax = 0;
        int trappedRainwater = 0;

        while (l <= r) {
            if (height[l] <= height[r]) {
                lMax = max(lMax, height[l]);
                trappedRainwater += lMax - height[l];
                l++;
            } else {
                rMax = max(rMax, height[r]);
                trappedRainwater += rMax - height[r];
                r--;
            }
        }

        return trappedRainwater;
    }
};



// lMax = 2
// rMax = 3

// [0,2,0,3,1,0,1,3,2,1]
//      l
//                r


// min(lMax, rMax) - height[i]