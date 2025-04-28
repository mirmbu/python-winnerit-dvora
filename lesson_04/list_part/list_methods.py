##append - insert to the end of list.
#grades = [100, 95, 80]
#print(f"{grades}")
#print(id(grades))
#grades.append(88)
#print(f"{grades}")
##id is stay as same
#print(id(grades))
from turtle import write_docstringdict
from xml.dom.minidom import ProcessingInstruction

##insert - insert to specific place
#grades.insert(0,57)
#grades.insert(2,78)
#grades.insert(6,92)
#print(f"{grades = }")

#Importana comment
#It is more efficient to use append because it adds to the end of the list.
#If you use insert to a specific location,
#you have to move all the indexes and this takes more time and space.


##remove - remove by value if exists.
#elemnt_to_remove = 80
#print(element_to_remove in grades) #return True if exists, False if not exist. in that way we can know if the value exist in the list or not.
#grades.remove(element_to_remove)
#print(f"{grades = }")
##grades.remove(81) #ValueError: list.remove(x): x not in list
#
#del grades[0]
#print(f"{grades = }")
#print(id(grades))

#pop
#remove_grade = []
#grades = [88, 100, 95, 80, 105]
#print(f"{grades = }")
#print(id(grades))
#
#remove_grade.append(grades.pop())
#print(f"{grades = }")
#print(id(grades))
#
#remove_grade.append(grades.pop(1))
#print(f"{grades = }")
#print(id(grades))
#
#print(f"{remove_grade = }")


##sort
#grades = [88, 100, 95, 80, 105]
#print(f"{grades = }")
#print(id(grades))
#
##sort from small to big
#grades.sort()
#print(f"{grades = }")
#print(id(grades))
#
##sort from big to small
#grades.sort(reverse=True)
#print(f"{grades = }")
#print(id(grades))

#String sorting - by ASCII
#words = ["AB", "bc", "BC", "Ab", "Zz", "ZZ"]
#print(f"{words = }")
#print(id(words))
#
#words.sort()
#print(f"{words = }")
#print(id(words))
#
#words.sort(reverse=True)
#print(f"{words = }")
#print(id(words))

#list words sorting - if all in lower letter, the sort work.
#words = ["banana", "apple", "cherry", "date"]
#print(f"{words = }")
#
#words.sort()
#print(f"{words = }")

#If exists upper letter, use the key str.lower
#words = ["banana", "Apple", "cherry", "Date"]
#print(f"{words = }")
#
#words.sort(key=str.lower)
#print(f"{words = }")


#reverse
#grades = [100, 95, 80, 105, 0]
#print(f"{grades[::-1] = }")
#print(f"{grades = }")
#grades.reverse()
#print(f"{grades = }")
