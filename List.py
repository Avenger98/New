a = []
for i in range(4):
    num = int(input("Enter the number: "))
    a.append(num)
print()
print("This is list created: ",a)

max = a[0]
min = a[0]

for numbers in a:
    if numbers > max:
        max = numbers
    if numbers < min:
        min = numbers

print()
print('This is the maximum number: ', max)
print('This is the minimum number: ', min)