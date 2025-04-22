hello_world = "Hello,world!"
#print(hello_world[0])
#print(hello_world[0:4]) #not include the 4th char, need to give 1 index above.
#print(hello_world[0:5])
#print(hello_world[:5])  #without start, start by default from 0
#print(hello_world[2:5])
#print(len(hello_world))
#print(hello_world[0:12])
#print(hello_world[0:-1])  #not give the last char, because allways its give the char before.
#print(hello_world[0:100]) #not error, give all the str.
#print(hello_world[:])     #all the str
#
##steps - skipping chars.
#print(hello_world[1:-1:1]) #skipping 1 chars
#print(hello_world[1:-1:2]) #skipping 2 chars
#print(hello_world[1:-1])   #by default its 1
#
##revers the str
#print(hello_world[::-1])
#print(hello_world)

#id
print(hello_world)
print(id(hello_world))
hello_world = "h" + hello_world[1:]
print(hello_world)
print(id(hello_world))