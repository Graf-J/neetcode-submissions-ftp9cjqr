class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l = 0;
        int r = heights.size() - 1;

        int currentMaxArea = 0;
        while (l < r) {
            currentMaxArea = max(currentMaxArea, min(heights[l], heights[r]) * (r - l));
            if (heights[l] < heights[r]) {
                l++;
            } else {
                r--;
            }
        }

        return currentMaxArea;
    }
};



// [1,7,2,5,4,7,3,6]
//  l      
//                r