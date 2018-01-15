from passenger import Passenger
from utilities import calc_direction, custom_max, custom_min

class Elevator(object):

    def __init__(self, n_floors, max_people = 10):
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
                print("Deleting Call",call[:3])
                self.add_destination(passenger) # adding dest and passenger
                self.calls.remove(call)
            passenger.time_cost += 1

        # Check for dropoffs (destination) on this floor
        for dest in self.destinations:
            passenger = dest[1]
            if dest[0] == self.floor:
                print("Deleting destination", dest[0])
                self.destinations.remove(dest)
            else:
                print("trying to find an edge case...")
                print(self.destinations, self.calls, self.destinations[0][1],self.direction)
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
            upwards_dropoffs_outside = [i[1] for i in self.calls if i[2] == 1]
            upwards_dropoffs_inside = [i[0] for i in self.destinations if i[0] >= self.floor]
            upwards_dropoffs = set(upwards_dropoffs_outside + upwards_dropoffs_inside)
            downwards_pickups = [i[0] for i in self.calls if i[2] == -1]
            max_up_dest = custom_max(upwards_dropoffs,downwards_pickups)
            while self.floor < max_up_dest:
                self.pickup_dropoff()
                self.move_one()
                print("floor",self.floor)
        elif self.direction == -1:
            downwards_dropoffs_outside = [i[1] for i in self.calls if i[2] == -1]
            downwards_dropoffs_inside = [i[0] for i in self.destinations if i[0] <= self.floor]
            downwards_dropoffs = set(downwards_dropoffs_outside + downwards_dropoffs_inside)
            upwards_pickups = [i[0] for i in self.calls if i[2] == 1]
            min_down_dest = custom_min(downwards_dropoffs,upwards_pickups)
            while self.floor > min_down_dest:
                self.pickup_dropoff()
                self.move_one()
                print("floor",self.floor)

    def max_floor_strategy(self):
        self.pickup_dropoff()
        while self.calls or self.destinations:
            for call in self.calls:
                print("Call")
                print(call[:3])
            self.move_to_max_min()
            self.direction = -self.direction
            self.pickup_dropoff()

    def add_call(self, call_floor, dest, Passenger):
        direction = calc_direction(call_floor, dest)
        self.calls.append([call_floor, dest, direction, Passenger])

    def add_destination(self, Passenger):
        self.destinations.append([Passenger.destination, Passenger])

    def snapshot(self):
        print("\nElevator Snapshot","\nCurrent Floor: ", self.floor, "\nDirection: ", self.direction, "\nDestinations: ", self.destinations)
