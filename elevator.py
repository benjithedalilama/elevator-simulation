from passenger import Passenger
from utilities import calc_direction

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

    def move_FIFO(self, target):
        self.floor = target

    def move_one(self):
        self.floor += self.direction

        # check for pickups on this floor
        for i in range(len(self.calls)):
            call = self.calls[i]
            passenger = call[3]
            if call[0] == self.floor and call[2] == direction:
                self.add_destination(call[1], passenger) # adding dest and passenger
                del self.calls[i]
            passenger.time_cost += 1

        # Check for dropoffs (destination) on this floor
        for i in range(len(self.destinations)):
            dest = self.destinations[i]
            passenger = dest[1]
            if dest[0] == self.floor:
                del self.destinations[i]
            passenger.time_cost += 1

    def FIFO(self):
        # Does this function loop over the calls? Looks like it doesnt
        # we need it to look at all of the calls, right?
        # should i do this in the simulation? how many times would I loop?
        # would i loop for the elevator calls? or destinations?
        """ Naive strategy: FIFO """
        first_call = self.calls[0]
        passenger = first_call[3]
        #move the Elevator towards next passenger in queue
        empty_elevator_dist = abs(self.floor - passenger.start_floor)
        self.move_FIFO(passenger.destination) #take the passeng er to its destinations
        # dont we have to delete the passenger just moved here?
        # like we are doing in the other strategy?
        # I guess in the sim we could just iterate over the calls but deletion is more clear and honest.
        distance = abs(passenger.start_floor - passenger.destination) #distance passenger traveled
        #update everyone's wait time_cost
        for call in self.calls:
            passenger.time_cost += distance + empty_elevator_dist

    def move_to_max_min(self):
        if self.direction == 1:
            up_floors = [i[1] for i in self.calls if i[2] == 1]
            dests = [i[0] for i in self.destinations]
            up_dest = max(max(up_floors), max(dests))
            while self.floor < up_dest:
                self.move_one()
        elif self.direction == -1:
            down_floors = [i[1] for i in self.calls if i[2] == -1]
            dests = [i[0] for i in self.destinations]
            down_dest = min(min(down_floors), min(dests))
            while self.floor < down_dest:
                self.move_one()

    def max_floor_strategy(self):
        while self.calls or self.destinations:
            self.move_to_max_min()
            self.direction = -1*self.direction #change direction

    def call(self, call_floor, dest, Passenger):
        direction = calc_direction(call_floor, dest)
        self.calls.append([call_floor, dest, direction, Passenger])

    def add_destination(self, Passenger):
        self.destinations.add(Passenger.destination, Passenger)
