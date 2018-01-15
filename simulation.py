import random
from elevator import Elevator
from passenger import Passenger
from building import Building

def main():
    num_passengers = int(input("How many passengers does the building have?"))
    num_floors = int(input("How many floors does the building have?"))
    strategy = int(input("Which strategy do you want to use? (1 for FIFO, 2 for move-to-max-min)"))
    building = Building(num_passengers, num_floors)
    elevator = Elevator(num_floors)
    for i in xrange(num_passengers):
        start_floor = random.choice(xrange(elevator.n_floors))
        destination_floor = random.choice(xrange(elevator.n_floors))
        while start_floor == destination_floor:
            destination_floor = random.choice(xrange(elevator.n_floors))
        passenger = Passenger(start_floor, destination_floor)
        elevator.call(passenger.start_floor, passenger.destination, passenger)
    if strategy == 1:
        elevator.FIFO


# main()
elevator = Elevator(10)
elevator.snapshot()
