def jump():
    turn_left()
    move()
    while wall_on_right():  # for variable wall height
        move()
    [turn_left() for i in range(3)]  # turn right
    move()  # crossing hurdle
    [turn_left() for i in range(3)]  # turn right
    while front_is_clear():
        move()  # descending
    turn_left()  # face forward


while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

# reeborg_hurdle4.py - completed in 164 moves
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
