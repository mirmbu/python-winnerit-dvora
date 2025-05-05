# Task 1:

age = int(input("Enter your age: "))
ticket = str(input("Do you have a ticket? (yes/no): "))
permission = str(input("Do you have special permission? (yes/no): "))

ticket = True if ticket == "yes" else False
permission = True if permission == "yes" else False

if age >= 18 and ticket == True:
    print("You can enter the club.")
elif age >= 18 and ticket == False:
    print("You cannot enter the club because you don't have a ticket.")
elif age < 18 and permission == True:
    print("You can enter the club with special permission.")
elif age < 18 and permission == False:
    print("You cannot enter the club.")


# Task 2:

num_1 = int(input("Please enter first number: "))
num_2 = int(input("Please enter second number: "))

result = num_1 if num_1 > num_2 else num_2
print(f"The larger number is: {result}")

# Task 3:
month = str(input("Enter a month: "))

match month:
    case "December" | "January" | "February":
        print("Winter")
    case "March" | "April" | "May":
        print("Spring")
    case "June" | "July" | "August":
        print("Summer")
    case "September" | "October" | "November":
        print("Autumn")
    case _:
        print("Invalid month")

# Task 4:
num = 0
summery = 0
for num in range(5):
    summery += int(input(f"Enter number {num+1}: "))

result = summery/(num+1)
print(f"The average is: {result}")

# Task 5:
def find_max(*args):
    max = 0
    if len(args) == 0:
        return "No numbers were given"
    else:
        for num in args:
            if num > max:
                max = num
        return max

print(find_max(8,5,3,9,1,6,0))

# Task 6:
def calculate_avarage(numbers):
    summery = 0
    i = 0
    for num in numbers:
        summery += num
        i += 1
    avg = summery/i
    return avg

numbers = [1,2,3,4,5,6,7,8,9,10]
print(calculate_avarage(numbers))