import utilities

class Passenger(object):

    def __init__(self, start_floor, destination):
        self.start_floor = start_floor
        self.destination = destination
        self.direction = utilities.calc_direction(start_floor, destination) ## to do
        self.time_cost = 0

    def increment_timecost(self, cost = 1):
        self.time_cost += cost
