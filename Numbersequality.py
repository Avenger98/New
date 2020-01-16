num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 == num2:
    if num2 == num3:
        print("They are all similar: ", num1,num2,num3)
    else:
        print("Number 1 and Number2 is equal, but not the number3: ", num1,num2,num3)
else:
    if num1 == num3:
        print("Num1 and Num3 is equal, but not the num2: ",num1,num2,num3)
    elif num2 == num3:
        print("the num2 and num3 are equal, but bot num1: ", num1,num2,num3)
    else:
        print("They r not equal",num1,num2,num3)