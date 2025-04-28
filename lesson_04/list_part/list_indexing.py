grade_winnerit = [100,50,60,98,80,79,45,96]
print(f"{grade_winnerit = }")

#indexs
#first
print(grade_winnerit[0])
#last
print(grade_winnerit[-1])
#also last
print(grade_winnerit[len(grade_winnerit) - 1])
#print(grade_winnerit[len(grade_winnerit)]) #error - IndexError: list index out of range

#slice
print(grade_winnerit[0:3])
print(grade_winnerit[3:])
print(grade_winnerit[::2])
print(grade_winnerit[::-1])
