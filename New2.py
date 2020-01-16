'''number1 = int(input("Enter the number1: "))
number2 = int(input("Enter the second number: "))
n1 = number1
n2 = number2

while number1 % number2 != 0:
    r = number1 % number2
    number1 = number2
    number2 = r
print(r)
print('First number:', n1, '\nSecond number:', n2)
print(n1/r, '/', n2/r)'''

numbers = input("Enter the two numbers: ")
b = numbers.split("/")
print(b)

number1 = int(b[0])
number2 = int(b[1])

while number1 % number2 != 0:
    r = number1 % number2
    number1 = number2
    number2 = r


print("GCD:", r)
print(int(b[0]) / r, '/', int(b[1]) / r)

