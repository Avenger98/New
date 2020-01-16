a = float(input("Enter the first catheter: "))
b = float(input("Enter the second catheter : "))
c = float(input("Enter the number for hypotenesis : "))

if (a**2) + (b**2) == (c**2):
    print("It can be right triangular")
else:
    print("Not right triangular")