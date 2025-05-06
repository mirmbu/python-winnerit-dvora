# list comprehension.
# a way to short way to create a list, based on a provided list.
# it combinates for loop and if condition.
# first part -> expression, what to do.
# middle part -> for loop on the list.
# last part -> if condition on each element. (optional)
# return all the elements that answer the condition.
# for example:

numbers = [1,2,3,4,5,6,7,8,9]
numbers2 = [60, 80, 90, 50, 45, 70, 90, 95, 70, 61, 30]

#like map()
new_list1 = [item ** 2 for item in numbers]
print(new_list1)


#lik filter()
new_list2 = [num for num in numbers2 if num >= 60]
print(new_list2)

#if the condition part is the middle - mean return all the elements, but the expression will be on the element that answer the condition.
#in those cases, need else.

new_list3 = [num ** 2 if num % 2 == 0 else num ** 0 for num in numbers]
print(new_list3)