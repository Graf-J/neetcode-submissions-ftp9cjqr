class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Sort cars closest to target first (memory efficient way with only one list)
        indices = list(range(len(position)))
        indices.sort(key=lambda x: position[x], reverse=True)

        # Process Cars
        num_fleets, cur_fleet_arrival = 0, -1
        for idx in indices:
            arrives_at = (target - position[idx]) / speed[idx]
            if arrives_at > cur_fleet_arrival: # New Fleet Starts
                num_fleets += 1
                cur_fleet_arrival = arrives_at

        return num_fleets



# Space-Complexity: O(N)
# Time-Complexity: O(N log(N) + N)

# Target = 10
# Cars = [(5, 2), (7, 4), (0, 10)]

# 1) Sort DESC -> O(n * log(n))

# num_fleets = 2
# cur_fleet_arrival = 2.5

# Cars = [(7, 4), (5, 2), (0, 10)]
#        [0.75  ,  2.5  ,  1     ]


# position: 7 miles
# speed: 4 miles/hour

# position(t) = position + speed * t
# Target = position + speed * t
# t = (Target - position) / speed

