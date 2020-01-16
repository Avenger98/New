list = ['Shoyira', 'Olimjon','Shakhina', 'Kakhramon']
list.append("John")
list.remove("John")
print(list)
print()
print(list[1])
print()
print(list[-1])
print()
# third one will not get executed and it is called range of indexes
print(list[2:3])
# -1 is not included Kakhramon is not included
print(list[-3:-1])
# list[1] changes the second element of the list
list[1] = "John"
print(list)

# for loop is used for writing out list elements
for x in list:
    print(x)
