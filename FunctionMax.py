def max(x,y,z):
    if x > y:
        if y>z:
            print("Max number is:", x)
        else:
            if x > z:
                print("Max number is:", x)
            else:
                print("Max number is:", z)
    else:
        if x > z:
            print("Max number is:", y)
        else:
           if z > y:
               print("Max number is:", z)
           else:
               print("Max number is:", y)
num1= int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
max(num1, num2, num3)
