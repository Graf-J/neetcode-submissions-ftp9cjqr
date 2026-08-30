class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<int> indices(position.size());
        iota(indices.begin(), indices.end(), 0);
        sort(indices.begin(), indices.end(), [&position](int i, int j) {
            return position[i] > position[j];
        });

        int numFleets = 0;
        float currentFleetArrival = -1;
        for (const auto& i : indices) {
            int s = position[i];
            int v = speed[i];
            float t_arrival = static_cast<float>(target - s) / v;

            if (t_arrival > currentFleetArrival) {
                numFleets++;
                currentFleetArrival = t_arrival;
            }
        }

        return numFleets;
    }
};





// s = 4; v = 2 -> t_arrival = 3
// s = 1; v = 3 -> t_arrival = 3


// t_arrival = (target - s) / v


// arrival = [5, 3, 10, 11, 9, 8]
// numFleets = 3
// currentFleetArrival = 11

