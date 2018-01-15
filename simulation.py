import random
from elevator import Elevator
from passenger import Passenger
from building import Building

def main():
    num_passengers = 10#int(input("How many passengers does the building have?"))
    num_floors = 10#int(input("How many floors does the building have?"))
    strategy = 2#int(input("Which strategy do you want to use? (1 for FIFO, 2 for move-to-max-min)"))
    building = Building(num_passengers, num_floors)
    elevator = Elevator(num_floors)
    passengers = []
    for i in range(num_passengers):
        start_floor = random.choice(range(elevator.n_floors))
        destination_floor = random.choice(range(elevator.n_floors))
        while start_floor == destination_floor:
            destination_floor = random.choice(range(elevator.n_floors))
        passenger = Passenger(start_floor, destination_floor)
        passengers.append(passenger)
        elevator.add_call(passenger.start_floor, passenger.destination, passenger)
    elevator.snapshot()
    print(elevator.calls)
    if strategy == 1:
        for passenger in passengers:
            elevator.FIFO()
            elevator.snapshot()
    else:
        elevator.max_floor_strategy()
        elevator.snapshot()
    for passenger in passengers:
            print(passenger.time_cost)

main()
