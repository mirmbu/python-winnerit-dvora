import datetime
# names = ["Michal", "Devora", "Ayala"]
#
# #basic function that print something. get 1 argument.
# def greet(name):
#     for name in names:
#         print(f"Hello {name}")
#
# greet(names)

# #TBD - To Be Done
# def get_text_from_element(element: any):
#     pass

# #1. No parameters and no return
# def say_hello():
#     print("Hello Everyone!")
#
# say_hello()


#2. Parameters and no return
#What we define in the definition of function -> parameters.
#What we pass to the function -> arguments.
# def say_hello_with_params(name, age):
#     print(f"Hello {name}! Your age is {age}")

# #say_hello_with_params() #TypeError: say_hello_with_params() missing 1 required positional argument: 'name'
# say_hello_with_params("Devora", 27) #pass the arguments in order (will print in order)
# say_hello_with_params(27, "Devora") #pass the arguments not in order (will print not in order)
# say_hello_with_params(age=27, name="Devora")   #pass the arguments not in order, but with the parameters (will print in order)

# def say_hello_with_params(name: str, age: float):
#     print(f"Hello {name.upper()}! Next year you will be {age + 1}")
#
# say_hello_with_params("Devora", 27)
# # say_hello_with_params("Devora", "27") #TypeError: can only concatenate str (not "int") to str

# def check_weather(city: str = "Jerusalem"):
#     print(f"Checking weather in {city}")
#     print(f"A weather is fine!")
#
# check_weather()
# check_weather("New york")

#3. Parameters and return
def calculate_sum(first_num: int, second_num: int) -> int | str:
    if first_num < 0 or second_num < 0:
        return "Invalid input"
    return first_num + second_num

#No print, because the function is only with return.
result = calculate_sum(10, 20)
print(result)
print(calculate_sum(10, 200))
print(calculate_sum(-1, 200))
#

# #4. Only return. no parameters.
# def get_current_time():
#     return datetime.datetime.now()
#
# print(get_current_time())


