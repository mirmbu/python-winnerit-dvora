#lower, upper
name = "AbcDEFG"
print(name.lower())
print(name.upper())

#strip - return the str without spaces
name_2 = "   AbcDEFG    "
print(name_2)
print(name_2.strip())

#replace
course = "Hello, Java!"
print(course.replace("Java", "Python"))

#split
courses = "Python Java JS"
print(courses.split()) #by default split by spaces

courses2 = "Python,Java,JS"
print(courses2.split(",")) #splite by ,

courses3 = "Python, Java, JS"
print(courses3.split()) #splite by spaces. the , insert to the list values.

#split to list and back to string.
courses = "Python Java JS"
corces_list = courses.split()
print(corces_list)
print(type(corces_list))
cources_string = " ".join(corces_list)
print(cources_string)
#
#find - if find str - return the index. if not - return -1
course = "Hello, Java!"
print(course.find("llo"))
print(course.find("hello")) #not find, because the string start with H.
#
##index
course = "Hello, Java!"
print(course.index("llo"))
#print(course.index("hello")) #error - substring not found
#
##startwith
course = "Hello, Java!"
print(course.startswith("Hello"))
print(course.startswith("hello"))
print(course.lower().startswith("Hello"))

#in
#course = "Hello, Java!"
print("llo" in course)
print("LLO" in course)