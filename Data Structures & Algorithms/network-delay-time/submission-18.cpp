class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<vector<pair<int, int>>> adj(n);
        for (const auto& time : times) {
            int u = time[0];
            int v = time[1];
            int t = time[2];
            adj[u - 1].push_back({v - 1, t});
        }

        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        pq.push({0, k - 1});

        vector<int> distances(n, numeric_limits<int>::max());
        distances[k - 1] = 0;

        int num_processed = 0;
        int max_delay = 0;
        while (!pq.empty()) {
            auto [t, node] = pq.top();
            pq.pop();
            
            if (distances[node] != t) continue;

            num_processed++;
            max_delay = max(max_delay, t);

            for (const auto& [neighbour, weight] : adj[node]) {
                if (t + weight < distances[neighbour]) {
                    distances[neighbour] = t + weight;
                    pq.push({t + weight, neighbour});
                }
            }
        }

        return num_processed == n ? max_delay : -1;
    }
};
