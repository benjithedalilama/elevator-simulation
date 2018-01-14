from passenger import Passenger

class Elevator(object):

    def __init__(self, n_floors):
        # initiating Elevator object with number of maximum floors in the building
        # starting at floor 0
        self.calls = []
        self.floor = 0
        self.n_floors = n_floors
        self.direction = None
        self.destinations = set([])

    def move_one(self, dest):
        # move to the next destination if it's on the same direction
        movement = direction(self.floor, dest)
        self.floor = self.floor + movement

        # check if there is a call in this floor
        for call in self.calls:
            if call[0] == self.floor:
                self.pickup(self.calls[2]) """ which is the person. need to program picking up people and weight"""

        # Check for dropoffs (destination) on this floor
        for dest in self.destinations:
            if dest[0] == self.floor:
                self.dropoff(dest[1]) #dest[1] is the Passenger

        #if direction(self.floor, dest) == self.direction:
        #self.floor += dest - self.curr_floor

    def call(self, call_floor, dest, Passenger):
        # append to calls log
        self.calls.append([call_floor, dest, Passenger])

    def add_destination(self, Passenger):
        """ need to implement destination as part of the Passenger class"""
        # for test: geenrating random destination:
        # uniformly_random_destination =  randint(self.floors_min, self.floors_max)
        self.destinations.add(Passenger.destination, Passenger)

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
