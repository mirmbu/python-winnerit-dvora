fruits = ['apple', 'banana', 'cherry', 'fig', 'date', 'kiwi', 'orange', 'grape']

def filter_words(args, num):
    fruits_list = list(x for x in args if len(x) >= num)
    return fruits_list

print(filter_words(fruits, 6))