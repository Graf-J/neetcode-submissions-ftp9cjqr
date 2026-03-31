class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        fleet_ctr = 1
        last_pos, last_vel = cars[0]
        last_duration = (target - last_pos) / last_vel
        for i in range(1, len(cars)):
            pos, vel = cars[i]
            duration = (target - pos) / vel
            if duration > last_duration:
                fleet_ctr += 1
                last_pos = pos
                last_vel = vel
                last_duration = duration

        return fleet_ctr