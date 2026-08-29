class Solution {
public:
    int trap(vector<int>& height) {
        int l = 0;
        int r = height.size() - 1;

        int lMax = height.front();
        int rMax = height.back();
        int trappedRainwater = 0;
        while (l < r) {
            if (height[l] < height[r]) {
                trappedRainwater += max(0, min(lMax, rMax) - height[l]);
                l++;
                lMax = max(lMax, height[l]);
            } else {
                trappedRainwater += max(0, min(lMax, rMax) - height[r]);
                r--;
                rMax = max(rMax, height[r]);
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