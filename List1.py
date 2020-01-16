cycle_number = int(input("Enter the cycle number: "))
a = []
for i in range(cycle_number):
    num = int(input("Enter the number: "))
    a.append(num)
print(a)

sum = 0
max = a[0]
min = a[0]
mult = 1
for i in a:
    sum += i
    mult *= i
    if i > max:
        max = i
    if i < min:
        min = i
print("Mult: ", mult)
print("Sum: ", sum)
print("Max: ", max)
print("Min: ", min)
