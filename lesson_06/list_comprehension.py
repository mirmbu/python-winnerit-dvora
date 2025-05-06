numbers = [1,2,3,4,5,6,7,8,9]
numbers2 = [60, 80, 90, 50, 45, 70, 90, 95, 70, 61, 30]

#first - expression - what to do.
#middle - for loop on the list.
#last - if condition on each element.
#return all the element that answer on the condition.

#like map()
new_list1 = [item ** 2 for item in numbers]
print(new_list1)


#lik filter()
new_list2 = [num for num in numbers2 if num >= 60]
print(new_list2)

#if the condition is the middle - mean return all the elements, but the expression will be on the element that answer the condition.
#also, need else.

new_list3 = [num ** 2 if num % 2 == 0 else num ** 0 for num in numbers]
print(new_list3)