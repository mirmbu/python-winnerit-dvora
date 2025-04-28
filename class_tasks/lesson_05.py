#Task 1
word_1 = str(input("Please enter a word: "))
word_2 = str(input("Please enter another word: "))

if word_1.lower() == word_2[::-1].lower():
   print("Yes")
else:
   print("No")

#Task 2:
salary = int(input("Enter your salary: "))
if salary >= 20000:
   print(f"{salary * 0.87}")
else:
   print(salary)

salary = salary * 0.87 if salary >= 20000 else salary
print(salary)

#Task 3:
num = int(input("Enter a number: "))
result_of = print("Even") if num % 2 == 0 else print("Odd")

#Task 4:
day = str(input("Enter a day: "))
match day.title():
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Weekday")
    case "Saturday" | "Sunday":
        print("Weekend")
    case _:
        print("Invalid day")

#Task 5:
numbers = [20,3,15,7,12,5]
for num in numbers:
    if num > 10:
        print(num)
    else:
        continue