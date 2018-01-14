import random
from elevator import Elevator
from passenger import Passenger
from building import Building

def main():
    num_passengers = int(input("How many passengers does the building have?"))
    num_floors = int(input("How many floors does the building have?"))
    building = Building(num_passengers, num_floors)
    elevator = Elevator(building.num_floors)
    for i in xrange(num_passengers):
        start_floor = 5
        destination_floor = 10
        passenger = Passenger(start_floor, destination_floor)
