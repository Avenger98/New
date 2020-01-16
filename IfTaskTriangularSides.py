num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 + num2 > num3:
    if num1 + num3 > num2:
        if num2 + num3 > num1 :
            print("It can be triangular")
        else:
            print("can not be triangular")
    else:
        print("can not be triangular")
else:
    print("can not be triangular")