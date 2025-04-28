user = "admin"
passw = "qwerty"

#username = input("Please enter your username: ")
#password = input("Please enter your password: ")
#
#if username == user and password == passw:
#    print("You ar logged in!")
#else:
#    print("You are not logged in!")


username = input("Please enter your username: ")
if username == user:
    password = input("Please enter your password: ")
    if password == passw:
        print("You ar logged in!")
    else:
        print("You are not logged in!")
else:
    print("You are not logged in!")


