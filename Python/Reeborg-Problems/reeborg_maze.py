# reeborg_maze: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# (Solution same as reeborg_hurdles4.py)
while not at_goal():
    if front_is_clear() and wall_on_right():
        move()
    elif not wall_on_right():
        [turn_left() for i in range(3)]  # turn right
        move()
    else:
        turn_left()
