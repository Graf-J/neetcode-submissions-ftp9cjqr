class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> result;
        deque<pair<int, int>> dq;

        for (int r = 0; r < nums.size(); ++r) {
            while (!dq.empty() and nums[r] >= dq.front().first) {
                dq.pop_front();
            }
            dq.push_front({nums[r], r});

            if (dq.back().second == r - k) {
                dq.pop_back();
            }

            if (r >= k - 1) {
                result.push_back(dq.back().first);
            }
        } 

        return result;
    }
};



    // {(1, 0)} // Empty -> Push-Left
    // {(2, 1)} // Bigger than left -> Pop & Push-Left
    // {(1, 2), (<2>, 1)} // Smaller than left -> Push-Left
    // {(0, 3), (1, 2), (<2>, 1)} // Smaller than left -> Push-Left
    // {(<4>, 4)} // Bigger than left -> Pop & Push-Left
    // {(2, 5), (<4>, 4)} // Smaller than left- -> Push-Left
    // {(6, <6>)} // Bigger than left -> Pop & Push-Left
