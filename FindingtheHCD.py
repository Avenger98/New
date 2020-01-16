# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
#
# r = 0
# while (num1 % num2) != 0:
#     r = num1 % num2
#     num1 = num2
#     num2 = r
# print(r)
num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))

r = 0

while num1 % num2 != 0:
    r = num1 % num2
    num1 = num2
    num2 = r
print(r)
