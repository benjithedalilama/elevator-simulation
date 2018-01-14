class Passenger(object):

    def __init__(self, current_floor, destination):
        self.current_floor = current_floor
        self.destination = destination
        self.direction = direction(current_floor, destination) ## to do
        self.time_cost = 0

    def increment_timecost(self, cost = 1):
        self.time_cost += cost

    def direction(current_floor, destination):
        # calculate the direction of movement based on start and end floors
        direction = None
        movement = destination - current_floor
        # calculate floors difference to determine direction:
        if movement > 0:
            direction = +1
        elif movement < 0:
            direction = -1
        else:
            # if destination is same as current floor, stay
            direction = 0
        return direction
