from passenger import Passenger
from utilities import calc_direction, target_floor

class Elevator(object):

    def __init__(self, n_floors, max_people = 10):
        # initiating Elevator object with number of maximum floors in the building
        # starting at floor 0
        self.calls = []
        self.floor = 0
        self.n_floors = n_floors
        self.direction = 1
        self.destinations = []
        self.max_people = max_people

    def move_FIFO(self, target):
        self.floor = target

    def move_one(self):
        self.floor += self.direction

    def pickup_dropoff(self):
        for call in self.calls:
            passenger = call[3]
            if call[0] == self.floor and call[2] == self.direction:
                self.add_destination(passenger) # adding dest and passenger
                call_to_delete = self.calls.index(call)
                del call_to_delete
            passenger.time_cost += 1

        # Check for dropoffs (destination) on this floor
        for dest in self.destinations:
            passenger = dest[1]
            if dest[0] == self.floor:
                print("DINDINDIN")
                dest_to_delete = self.destinations.index(dest)
                print(dest_to_delete)
                del dest_to_delete
            passenger.time_cost += 1

    def FIFO(self):
        first_call = self.calls[0]
        passenger = first_call[3]
        #move the Elevator towards next passenger in queue
        empty_elevator_dist = abs(self.floor - passenger.start_floor)
        self.move_FIFO(passenger.destination) #take the passeng er to its destinations
        distance = abs(passenger.start_floor - passenger.destination) #distance passenger traveled
        #update everyone's wait time_cost
        for call in self.calls:
            call[3].time_cost += distance + empty_elevator_dist
        del self.calls[0]

    def move_to_max_min(self):
        if self.direction == 1:
            up_floors = [i[1] for i in self.calls if i[2] == 1]
            dests = [i[0] for i in self.destinations]
            up_dest = max(target_floor(up_floors,self.direction,self.n_floors), target_floor(dests,self.direction,self.n_floors))
            while self.floor < up_dest:
                self.move_one()
                self.pickup_dropoff()
        elif self.direction == -1:
            down_floors = [i[1] for i in self.calls if i[2] == -1]
            dests = [i[0] for i in self.destinations]
            down_dest = min(target_floor(down_floors,self.direction,self.n_floors), target_floor(dests,self.direction,self.n_floors))
            while self.floor < down_dest:
                self.move_one()
                self.pickup_dropoff()

    def max_floor_strategy(self):
        while self.calls or self.destinations:
            for call in self.calls:
                print(call[0], call[1])
            self.move_to_max_min()
            self.direction = -self.direction
            break

    def add_call(self, call_floor, dest, Passenger):
        direction = calc_direction(call_floor, dest)
        self.calls.append([call_floor, dest, direction, Passenger])

    def add_destination(self, Passenger):
        self.destinations.append([Passenger.destination, Passenger])

    def snapshot(self):
        print("\nElevator Snapshot","\nCurrent Floor: ", self.floor, "\nDirection: ", self.direction, "\nDestinations: ", self.destinations)
