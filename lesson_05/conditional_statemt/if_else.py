#if basic
#age = 19
#if age >=19:
#    print("You can enter")
#
#print("After if")

#if else basic
#age = int(input("Enter your age: "))
#if age >= 19:
#    print("You can enter")
#else:
#    print("You cannot enter")

#elif basic
#age = int(input("Enter your age: "))
#if age > 18:
#    print("You can enter")
#elif 14<= age <= 18:
#    print("You need your parents")
#else:
#    print("You cannot enter")
#print("After if-else")

#if else versus
#age = int(input("Enter your age: "))
#if age > 18:
#    print("You can enter")
#if age > 14:
#    print("You need your parents")
#else:
#    print("You cannot enter")
#print("After if-else")

#pass
age = int(input("Enter your age: "))
if 18 < age <= 67:
    print("You can enter")
elif 14< age <= 18:
    print("You need your parents")
#there is a condition, but not do anything. wait to future development.
elif age > 67:
    pass
else:
    print("You cannot enter")
print("After if-else")