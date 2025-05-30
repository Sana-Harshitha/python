fruit = input("Enter Your Fruit Name: ")
fruit_color = input(f"Enter Your {fruit} Color: ")
fruit_color = fruit_color.strip().lower()
fruit = fruit.strip().lower()
if fruit == "banana":
    if fruit_color == "green":
        print("Unripe")
    elif fruit_color == "yellow":
        print("Ripe")
    elif fruit_color == "brown":
        print("OverRipe")
    else:
        print("Unknown banana color")
else:
    print(f"I don't have info about {fruit}.")
