def is_Even_or_Odd(number):
    if number % 2 == 0:
        print("This number is even :", number)
    else:
        print("The number entered is odd: ", number)


num = int(input("Enter the number: "))
x = num
is_Even_or_Odd(x)
