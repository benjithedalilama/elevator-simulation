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
        # move 1 floor in direction (direction is +1 or -1 floors)
        movement = direction(self.floor, dest)
        self.floor = self.floor + movement

        # check if there is a call in this floor
        # ** this checks the last element in the calls list, assuming we append to it!
        for call in self.calls:
            # Check for pickups on that floor
            if call[0] == self.floor:
                # if the last call is from this floor pickup person
                self.pickup(self.calls[2]) """ which is the person. need to program picking up people and weight"""
                #self.add_rand_destination()

        # Check for dropoffs (destination) on this floor
        for dest in self.destinations:
            # check for destinations and dropoff
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

    # def pickup(self,Passenger):
    #     self.add_rand_destination(self)
    #     # add random weight
    #     """ change this to person's weight when we have that class and simulaiton"""
    #     self.weight += Passenger.weight # change to self.weight += Passenger.weight
    #     return "I don't know yet what does picking up passengers really mean."
    #
	# def dropoff(self,Passenger):
    # 	self.weight -= Passenger.weight
    # 	return "I don't know yet what does picking up passengers really mean."

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
