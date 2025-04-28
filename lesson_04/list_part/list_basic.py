#not comfort
#grade_by_dvora = 100
#grade_by_alex = 80
#grade_by_ayala = 90

#list - mutable - can change the list. 
#grade_winnerit = [100,50,60,98,80]
#print(f"{grade_winnerit = }")
#print(id(grade_winnerit))
#
#grade_winnerit[2] = "Dvora"
#print(f"{grade_winnerit = }")
#print(id(grade_winnerit))
#
#grade_winnerit_2 = [100, "Text", True, 60, [50, 45]]
#print(f"{grade_winnerit_2 = }")

grades = [100, "Text", True, 60, [50, 45]]
print(f"{grades = }")
print(grades[0]-5)
#print(grades[1] - 5) #error - TypeError: unsupported operand type(s) for -: 'str' and 'int'

