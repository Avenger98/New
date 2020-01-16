number1 = int(input("Enter the number1: "))
number2 = int(input("Enter the number2: "))
r = 0
while number1 % number2 != 0:
    r = number1 % number2
    number1 = number2
    number2 = r
print(r)
