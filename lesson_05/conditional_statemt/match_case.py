#example 1
color = input("Enter a color: ")

#if-else
if color == "red":
    print("stop")
elif color == "yellow":
    print("Cavtion")
elif color == "green":
    print("Go")
else:
    print("Unknown color")

#match-case
match color:
    case "red":
        print("Stop")
    case "yellow":
        print("Cavtion")
    case "green":
        print("Go")
    case _:
        print("Unknown color")

#example 2:
fruit = input("Enter a fruit: ")

match fruit:
    case "apple" | "banana" | "orange":
        print("Common fruits")
    case "mango" | "pineapple":
        print("Tropical fruits")
    case _:
        print("Unknown fruit")

#if there is many conditions, try to use design patterns
#https://refactoring.guru/design-patterns/factory-method/python/example
