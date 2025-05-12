import math
#1.
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
new_list = [num ** 2 for num in numbers_list if num % 2 == 0]
print(new_list)

#2.
word_list = ['hello', 'world', 'python', 'programming', 'is', 'awesome']
new_word_list = [word for word in word_list if len(word) > 5]
print(new_word_list)

#3.
str_list = ['hello', 'world', 'python', 'programming', 'is', 'awesome']
new_str_list = [word.upper() for word in str_list]
print(new_str_list)

#4.
int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
str_int_list = [str(i) for i in int_list]
print(str_int_list)

#5.
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
three_list = [num * 10 for num in num_list if num%3==0]
print(three_list)

#6.
mat_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
array_list = [num for row in mat_list for num in row]
print(array_list)

#7.
string = 'hello world'
new_string = [char for char in string if char != ' ']
print(new_string)

#8.
names = ["Devora", "Lea", "Ayala", "Michal", "Ester", "Adina", "Ahuva"]
name_a = [name for name in names if name.startswith('A')]
print(name_a)

#9.
list_i = [1, 2, 3]
list_j = [4, 5, 6]
dic = [(i, j) for i in list_i for j in list_j]
print(dic)

#10.
numbers_list = range(1, 100)
perfect_numbers_list = [num for num in numbers_list if math.isqrt(num) ** 2 == num]
print(perfect_numbers_list)