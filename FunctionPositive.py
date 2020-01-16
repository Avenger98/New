def is_positive(number):
    if number < 0:
        print("the number entered is negative :", number)
    else:
        print("The number entered is positive :", number)


num1 = int(input("Enter the number: "))
y = num1
is_positive(y)
