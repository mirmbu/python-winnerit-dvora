#when not use - when have long or difficult statement.

num = 7
result_of = ""

if num % 2 == 0:
    result_of = "Even"
else:
    result_of = "Odd"

print(result_of)

#example even/odd
result_of = print("Even") if num % 2 == 0 else print("Odd")
#print(result_of)

#example max_value
x, y = 10, 20
max_value = x if x > y else y
print(max_value)

#example - in this case it better to use regular if-else because it more readable.
num = 0
if num > 0:
    print("Positive value")
elif num < 0:
    print("Negative value")
else:
    print("Zero value")

res = "Positive value" if num > 0 else "Negative value" if num < 0 else "Zero value"
print(res)