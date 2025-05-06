# #lambda function is anonymous function.
# calculation = lambda x: x ** 3
# result = calculation(3)
# print(result)
#
# calculation2 = lambda x, y: x ** y
# result2 = calculation2(5, 3)
# print(result2)
#
# def calculation2_not_lambda(x, y):
#     result3 = x ** y
#     return result3
# print(calculation2_not_lambda(5,3))


# #map() with lambda
# #map is function that do any action on every element in a list.
# #used usually in lambda expression.
# #example with lambda -> square each element in the list.
# numbers = [1,2,3,4,5]
# squared_numbers = list(map(lambda x: x ** 2, numbers))
# print(squared_numbers)
#
# #same exemple with map() that call a function.
# def squared_number2(x: int):
#     return x ** 2
#
# result = list(map(squared_number2, numbers))
# print(result)
#
# #function that do same thing as map.
# def work_with_list(list_of_nums: list[int]):
#     new_list = []
#     for num in list_of_nums:
#         new_list.append(num ** 2)
#     return new_list
# print(work_with_list(numbers))


#filter
#return all the elements that answer on the condition
num_to_filter = [60, 80, 90, 50, 45, 70, 90, 95, 70, 61, 30]

def filter_numbers(x: int):
    return x >= 60

filter_result = list(filter(lambda x: x>= 60, num_to_filter))
print(filter_result)

filter_result2 = list(filter(filter_numbers, num_to_filter))
print(filter_result2)

def work_with_list(list_of_nums: list[int]):
    new_list = []
    for num in list_of_nums:
        if num >= 60:
            new_list.append(num)
    return new_list

print(work_with_list(num_to_filter))
