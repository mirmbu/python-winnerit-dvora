#booleans
from pickle import FALSE

#print(True)          #True
#print(False)         #False
#print(bool(1))       #True
#print(bool(-2))      #True
#print(bool(0))       #False - only 0 give false
#print(bool(""))      #False - empty string
#print(bool(" "))     #True - string with space - not empty
#print(bool("True"))  #True
#print(bool("False")) #True - the string is "False", but it not empty string, so it "True"

#operators
#print("==")
#print(5==5) #True
#print(5==6) #False
#
#print(">")
#print(5>5) #False
#print(5>6) #False
#print(5>4) #True
#
#print("<")
#print(5<5) #False
#print(5<6) #True
#print(6<5) #False
#
#print("<=")
#print(5<=5) #True
#print(5<=6) #True
#print(6<=5) #False
#
#print(">=")
#print(5>=5) #True
#print(5>=6) #False
#print(5>=4) #True
#
#print("!=")
#print(5!=5) #False
#print(5!=6) #True

#logical operator in Java && !!
#bitwise operator & |

#logical operator in Python and, or, not,
#and
#print(f"True and True = {True and True}")
#print(f"True and False = {True and False}")
#print(f"False and True = {False and True}")
#print(f"False and False = {False and False}")
#print(f"True and True and False = {True and True and False}")
#
#username = input("Enter username: ")
#password = input("Enter password: ")
#
##if the input will be the value - will get true, if not - false.
#print(username == 'user' and password == 'yes')

##or
#print(f"True or True = {True or True}")
#print(f"True or False = {True or False}")
#print(f"False or True = {False or True}")
#print(f"False or False = {False or False}")
#print(f"True or True or False = {True or True or False}")
#             #True      or     #False
#print(f"(True or False) or True and False = {(True or False) or True and False}")

#not
#print(f"not True = {not True}")
#print(f"not False = {not False}")