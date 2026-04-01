from collections import namedtuple
from itertools import islice

Car = namedtuple("Car", ["position", "speed"])

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted((Car(*x) for x in zip(position, speed)), reverse=True)
        prev_time = (target - cars[0].position) / cars[0].speed
        fleet_ctr = 1 # Because the first car already represents a fleet
        for car in islice(cars, 1, None):
            current_time = (target - car.position) / car.speed
            if car_ahead_is_faster := prev_time < current_time:
                fleet_ctr += 1 # Adds a fleat every time there is a gap
                prev_time = current_time  # New car is new slow car other cars catch up

        return fleet_ctr

# Car-1: distance = pos + speed * t

# t = (distance - pos) / speed