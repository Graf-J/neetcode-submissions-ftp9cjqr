class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        num_fleets = 0
        t_prev_fleet = float("-inf")
        for car_pos, car_vel in cars:
            t_car = (target - car_pos) / car_vel
            if t_car > t_prev_fleet:
                num_fleets += 1
                t_prev_fleet = t_car

        return num_fleets