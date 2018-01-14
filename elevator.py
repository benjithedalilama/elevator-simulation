from passenger import Passenger

class Elevator(object):

    def __init__(self, n_floors, max_people = 10):
        # initiating Elevator object with number of maximum floors in the building
        # starting at floor 0
        self.calls = []
        self.floor = 0
        self.n_floors = n_floors
        self.direction = None
        self.destinations = set([])
        self.max_people = max_people

    def move_FIFO(self, dest):
        self.floor = dest

    def move_one(self, dest):
        self.floor += self.direction
        stopped = 0

        # check for pickups on this floor
        for i in range(len(self.calls)):
            call = self.calls[i]
            if call[0] == self.floor and call[2] == direction:
                del self.calls[i]
                stopped = 1

        # Check for dropoffs (destination) on this floor
        for i in range(len(self.destinations)):
            dest = self.destinations[i]
            if dest[0] == self.floor and dest[2] == direction:
                del self.destinations[i]
                stopped = 1

        cost = 1 + stopped

    def move_one(self, dest):
        # move to the next destination if it's on the same direction
        movement = direction(self.floor, dest)
        initial_floor = self.floor
        self.floor = self.floor + movement
        distance = self.floor - initial_floor
        stopped = 0
        # check if there is a call in this floor
        for call in self.calls:
            if call[0] == self.floor:
                self.pickup(self.calls[2]) """ which is the person. need to program picking up people and weight"""
                stopped = 1

        # Check for dropoffs (destination) on this floor
        for dest in self.destinations:
            if dest[0] == self.floor:
                self.dropoff(dest[1]) #dest[1] is the Passenger
                stopped = 1

        #for call in self.calls:
        #    passenger = call[2]
        #    cost = distance + stopped ## cost is the distance plus 1 if the elevator stopped at the destination
        #    passenger.time_cost += cost


        #if direction(self.floor, dest) == self.direction:
        #self.floor += dest - self.curr_floor

    def naive_strat(self):
        # while there are calls, pickup fi
        while len(self.calls) > 0:
            call_floor = self.calls[0][0]
            call_dest = self.calls[0][1]
            passenger = self.
            move_one(self, call_dest)

    def call(self, call_floor, dest, Passenger):
        # append to calls log
        direction = calc_direction(call_floor, dest)
        self.calls.append([call_floor, dest, direction, Passenger])

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
