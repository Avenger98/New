import file as Django

name = input("Enter ur name: ")

Django.displayMsg(name)

a = int(input("Enter a value for a: "))
b = int(input("Enter a value for b: "))

Django.summation(a, b)

print(Django.minus(a, b))
print(Django.division(a, b))


List = dir(Django)
print(List)
