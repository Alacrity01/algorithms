def jump():
    move()
    turn_left()
    move()
    [turn_left() for i in range(3)]  # turn right
    move()
    [turn_left() for i in range(3)]  # turn right
    move()
    turn_left()


[jump() for _ in range(6)]
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
