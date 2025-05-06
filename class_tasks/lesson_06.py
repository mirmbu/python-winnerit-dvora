# #Task 1:
# numbers = [1,2,3,4,5,6,7,8,9,10]
#
# #filter with regular function
# def filter_even(numbers):
#     new_list = []
#     for num in numbers:
#         if num % 2 ==0:
#             new_list.append(num)
#     return new_list
#
# print(filter_even(numbers))
#
# #filter with list comprehensions
# filter_list = [num for num in numbers if num % 2 ==0]
# print(filter_list)
#
# #filter with lambda function
# lambda_filter = list(filter(lambda num: num % 2 == 0, numbers))
# print(lambda_filter)
#
# #Task 2: