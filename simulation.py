import random
from elevator import Elevator
from passenger import Passenger
from building import Building

def main():
    num_passengers = int(input("How many passengers does the building have?"))
    num_floors = int(input("How many floors does the building have?"))
    building = Building(num_passengers, num_floors)
    elevator = Elevator(num_floors)
    call_list = []
    for i in xrange(num_passengers):
        start_floor = random.choice(xrange(elevator.n_floors))
        destination_floor = random.choice(xrange(elevator.n_floors))
        while start_floor == destination_floor:
            destination_floor = random.choice(xrange(elevator.n_floors))
        passenger = Passenger(start_floor, destination_floor)
        call_list.append(passenger)

main()
