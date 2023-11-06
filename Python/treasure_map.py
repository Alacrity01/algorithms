line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")

# Where do you want to put the treasure?
position = input("Where do you want to put the treasure? \n").casefold()
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
# position = "B3"
d = {"a": 0,
     "b": 1,
     "c": 2,
     "1": line1,
     "2": line2,
     "3": line3}

row = d[position[1]]
col = d[position[0]]

row[col] = "X"
# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
