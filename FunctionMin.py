def min(x,y,z):
    if x > y:
        if y>z:
            print("Min number is:", z)
        else:
            if x > z:
                print("Min number is:", y)
            else:
                print("Min number is:", y)
    else:
        if x > z:
            print("Min number is:", z)
        else:
           if z > y:
               print("Min number is:", x)
           else:
               print("Min number is:", x)
num1= int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
min(num1, num2, num3)
