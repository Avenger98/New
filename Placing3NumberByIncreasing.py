a = int(input("Enter a value for a: "))
b = int(input("Enter a value for b: "))
c = int(input("Enter a value for c: "))

if a>b :
    if b>c:
        print(a, b, c)
    else:
        if a>c:
            print(a,c,b)
        else:
            print(c,a,b)
else:
    if a > c:
        print(b,a,c)
    else:
        if b>c :
            print(b,c,a)
        else:
            print(c,b,a)
