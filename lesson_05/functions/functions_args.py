names = ["Michal", "Devora", "Ayala"]

# #basic function that print something. get 1 argument.
# def greet(name: list[str]):
#     for name in names:
#         print(f"Hello {name}")
#
# greet(names)

#When pass args to function, it will pass it as tuple.
#there is not so many difference between tuple to list
#but need to notice to the type. that for list (of string) there are many methods and for tuple only 2 methods.
def greet(*args):
    print(args)
    print(type(args))
    for name in args:
        print(f"Hello {name}")

greet("Michal", "Devora", "Ayala", "Alex")