
#1D
#fruits =        ["Apple", "Orange", "Pear", "Banana"]
#vegetables =    ["Apple", "Orange", "Pear", "Banana"]
#meats =         ["Chicken", "Pork", "Fish"]

#groceries = [fruits, vegetables, meats]

#2D
groceries = [["Apple", "Orange", "Pear", "Banana"],
             ["Apple", "Orange", "Pear", "Banana"],
             ["Chicken", "Pork", "Fish"]]

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()