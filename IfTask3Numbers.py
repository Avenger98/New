a = int(input("Enter the first number: "))
b = int(input("Enter the first number: "))
d = int(input("Enter the first number: "))

if a > b:
    if b > d:
        print(a, b, d)
    else:
        if a > d:
            print(a, d, b)
        else:
            print(d, a, b)
else:
    if b > d:
        if a > d:
            print(b, a, d)
        else:
            print(b, d, a)
    else:
        print(d, b, a)
