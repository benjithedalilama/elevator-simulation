def calc_direction(current_floor, destination):
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
