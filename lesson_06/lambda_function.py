# lambda
# A lambda function (or anonymous function) is a small, anonymous function that can be defined in one line.
# Can have any number of arguments but can only have one expression.
# Need to assign it, because if not, we don't have a name to refer to it.
# Example:
#  This alone doesn't work - the lambda is created but can't be called
lambda x: x ** 3

# This works because we store the lambda in a variable
calculation = lambda x: x ** 3
result = calculation(3) #Output = 27
print(result)

# This also works because we immediately print the lambda function.
print((lambda x: x ** 3)(3)) #Output = 27


def calculation_not_lambda(x, y):
    result_not_lambda = x ** y
    return result_not_lambda
print(calculation_not_lambda(3,3)) #Output = 27


# map() with lambda
# map is a function that does any action on each element in a list.
# can get a list or call a function.
# used usually in lambda expression.
# an example with lambda -> square each element in the list.
numbers = [1,2,3,4,5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)

# same exemple with map() that call a function.
def squared_number2(x: int):
    return x ** 2

result = list(map(squared_number2, numbers))
print(result)

# a function that does the same thing as map() function.
def work_with_list(list_of_nums: list[int]):
    new_list = []
    for num in list_of_nums:
        new_list.append(num ** 2)
    return new_list
print(work_with_list(numbers))


# filter
# is a function that filters elements in a list by a condition.
# example with lambda -> filter out all elements in the list that are less than 60.
num_to_filter = [60, 80, 90, 50, 45, 70, 90, 95, 70, 61, 30]

filter_result = list(filter(lambda x: x>= 60, num_to_filter))
print(filter_result)

# same example with lambda that call a function.
def filter_numbers(x: int):
    return x >= 60

filter_result2 = list(filter(filter_numbers, num_to_filter))
print(filter_result2)

# a function that does the same thing as filter() function.
def work_with_list(list_of_nums: list[int]):
    new_list = []
    for num in list_of_nums:
        if num >= 60:
            new_list.append(num)
    return new_list

print(work_with_list(num_to_filter))
