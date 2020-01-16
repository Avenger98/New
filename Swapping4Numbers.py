a = int(input('Enter the value for a: '))
b = int(input('Enter the value for b: '))
c = int(input('Enter the value for c: '))
d = int(input('Enter the value for d: '))

if  a>b:
    temp = a
    a = b
    b = temp
if b>c:
    temp = b
    b = c
    c = temp
if c>d:
    temp = c
    c = d
    d =temp
if a > b:
   temp = a
   a = b
   b =temp
if b > c :
    temp = b
    b = c
    c =temp
if a > b:
    temp = a
    a = b
    b =temp

print(a)
print(b)
print(c)
print(d)