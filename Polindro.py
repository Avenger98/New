'''name = input("Enter the name: ")

if name[0] == name[-1]:
    print("It is a polindrom")
else:
    print("It is not a polindrom")
'''

found =False
name = input("Enter the word: ")
'''
for counter in range(len(name)//2):
    if name[counter] != name[-counter-1]:
        found = True
        print("Not Polindrom")
if not found:
    print("Polindrom")
'''
found = False
name = input("Enter the word: ")
z = ""
for i in name:
    z = i + z
    if z == name:
        found = True
        print("It is Polindrom")
    else:
         print("Ie is not a polindrom")



