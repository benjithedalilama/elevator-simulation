class Passenger(object):

    def __init__(self, current_floor, target_floor, weight = 60, distance_traveled):
        self.current_floor = current_floor
        self.target_floor = target_floor
        self.weight = weight
        self.time_cost = 0

    def increment_timecost(self, cost = 1):
        self.time_cost += cost
        
