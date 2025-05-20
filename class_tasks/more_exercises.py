import math
from datetime import datetime
from functools import reduce

#List comprehensions
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

#Lambda
#1.
number = lambda x: x ** 2
print(number(5))

#2.
small_num = lambda x, y: x if x < y else y
print(small_num(5, 10))

#3.
revers_word = lambda word: word[::-1]
print(revers_word("hello"))

#4.
numbers = [11,2,3,4,54,6,7,8,9,10]
max_num = reduce(lambda x, y: x if x > y else y, numbers)
print(max_num)

#5.
word_list = ["Dvora", "Hirshaut", "27", "age", "name"]
min_word = min(word_list, key=lambda word: len(word))
print(min_word)

#6.
numbers = [1, 2, 3, 4, 5, 6, 7]
triple_number = list(filter(lambda x: x % 3 == 0, numbers))
print(triple_number)

#7.
numbers = [1, -2, 3, -4, 5, -6, 7]
positive_number = sum(filter(lambda x: x > 0, numbers))
print(positive_number)

#8.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
multi_number = list(map(lambda x: x * 2, numbers))
print(multi_number)

#9.
dates_list = ["11.01.2023", "12.01.2023", "13.01.2023", "14.01.2023", "15.01.2022"]
datetime_list = list(map(lambda date: datetime.strptime(date, "%d.%m.%Y"), dates_list))
earliest_date = min(datetime_list)
print(earliest_date)

#10.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_devided_5 = list(filter(lambda x: x % 5 == 0, numbers))
print(numbers_devided_5)

#11.
words = ["banana", "apple", "orange", "kiwi", "melon", "mango"]
even_word = list(filter(lambda word: len(word) % 2 ==0, words))
min_word = min(even_word, key=lambda word: len(word))
print(min_word)

#12.
numbers = [123, 7, 45678, 90, -12345, 1000]
str_list = list(map(lambda num: str(abs(num)), numbers))
max_num = max(str_list, key=lambda num: len(num))
print(max_num)

#13.
dates = ['05-01-2020','25-12-2019','15-01-2022','01-01-2021','10-02-2020']
datetime_list = list(map(lambda date: datetime.strptime(date, '%d-%m-%Y'), dates))
jenuray_dates = list(filter(lambda date: date.month == 1, datetime_list))
date = min(jenuray_dates)
print(date)

#14.
numbers = [11,22,35,48,60,17,90,13]
max_num = max(list(filter(lambda num: num % 2 ==0, numbers)))
print(max_num)

#15.
words = ["hello", "education", "umbrella", "sky", "apple", "rhythm"]
vowels = ["a", "e", "i", "o", "u"]
max_word = max(words, key=lambda word: len(list(filter(lambda letter: letter in vowels, word))))
print(max_word)

max_word2 = max(words, key=lambda word: sum(letter in 'aeiou' for letter in word))
print(max_word2)